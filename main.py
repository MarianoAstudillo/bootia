import os
import sys, traceback
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function
from functions.schemas import schema_get_files_info
from functions.schemas import schema_get_file_content
from functions.schemas import schema_run_python_file
from functions.schemas import schema_write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def request_gemini(prompt, verbose_f, model='gemini-2.0-flash-001'):
    
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )

    response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        ),
    )

    if response.function_calls is not None and len(response.function_calls) > 0:
        for function_call_part in response.function_calls:
            call_result = call_function(function_call_part, True)
            if not hasattr(call_result, "parts"):
                raise Exception('Fatal Error: No response')
            
            if verbose_f is True:
                print(f"-> {call_result.parts[0].function_response.response}")
    else: 
        print(f"{response.text}")

    if verbose_f is True:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def main():
    verbose_flag = False;
    try:
        if len(sys.argv) <= 1:
            raise Exception("Need a prompt")

        if len(sys.argv) >= 3:
            if '--verbose' in sys.argv[2]:
                verbose_flag = True

        
        request_gemini(sys.argv[1], verbose_flag)
    except:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
