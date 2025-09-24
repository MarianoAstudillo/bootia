import os
import sys, traceback
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def request_gemini(prompt, verbose_f, model='gemini-2.0-flash-001'):
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model=model, 
        contents=messages
    )
    print(response.text)

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
