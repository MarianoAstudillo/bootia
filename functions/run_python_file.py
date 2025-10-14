import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):
  try:
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)
    abs_working_directory = os.path.abspath(working_directory)
    
    if not abs_full_path.startswith(abs_working_directory):
      raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(full_path):
      raise Exception(f'Error: File "{file_path}" not found.')
    if file_path[-3:] != '.py':
      raise Exception(f'Error: "{file_path}" is not a Python file.')

    try:
      result = subprocess.run(
        [f'uv run {file_path}', " ".join(args)],
        cwd=working_directory,
        timeout=30,
        capture_output=True,
        shell=True
      )

      result_string = f'STDOUT: {result.stdout}, STDERR: {result.stderr}'

      if result.returncode != 0:
        result_string + f', Process exited with code {result.returncode}'

      if not result:
        return 'No output produced.'

    except Exception as e:
      return f"Error: executing Python file: {e}"

    return result_string

  except Exception as e:
    # print(f'Error: {e}')
    return e
    # return f"Error: executing Python file: {e}"