import os
import sys

from functions.config import *

def write_file(working_directory, file_path, content):
  try:
    full_path = os.path.join(working_directory, file_path)
    dirname_path = os.path.dirname(os.path.abspath(full_path))

    if not os.path.exists(dirname_path):
      os.makedirs(dirname_path, mode=0o777, exist_ok=True)
    
    if not full_path.startswith(working_directory):
      raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    with open(full_path, "w") as f:
      f.write(content)
      return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

  except Exception as e:
    print(f'Error: {e}')
  