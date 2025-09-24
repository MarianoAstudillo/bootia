import os
import sys

from functions.config import *

def get_file_content(working_directory, directory):
  try:
    print(f'working_directory: {working_directory}')
    print(f'directory: {directory}')

    full_path = os.path.join(working_directory, directory)

    if os.path.isdir(full_path):
      raise Exception(f'"{full_path}" is not a directory')

    # Normalize both paths
    full_path = os.path.abspath(full_path)
    working_directory = os.path.abspath(working_directory)
    
    if not full_path.startswith(working_directory):
      raise Exception(f'Cannot read "{full_path}" as it is outside the permitted working directory')

    is_file = os.path.isfile(full_path)
    if not is_file:
      raise Exception(f'Error: File not found or is not a regular file: "{full_path}"')

    with open(full_path, "r") as f:
      file_content_string = f.read()
      if len(file_content_string) > MAX_CHARS:
        return f'{file_content_string[:MAX_CHARS]} [...File "{full_path}" truncated at 10000 characters].'

      return file_content_string

  except Exception as e:
    print(f'Error: {e}')
  