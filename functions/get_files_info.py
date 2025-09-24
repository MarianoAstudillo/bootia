import os
import sys

def get_files_info(working_directory, directory="."):
  try:

    # Build the full path
    full_path = os.path.join(working_directory, directory)

    if not os.path.isdir(full_path):
      raise Exception(f'"{directory}" is not a directory')

    # Normalize (remove .., symbolic links, etc.)
    full_path = os.path.abspath(full_path)
    working_directory = os.path.abspath(working_directory)

    # Validation: is full_path still inside working_directory?
    if not full_path.startswith(working_directory):
      raise Exception(f'Cannot list "{directory}" as it is outside the permitted working directory')

    # Check all found dirs in path
    list_dirs = []
    for dir_file in os.listdir(full_path):
      dir_file_path = os.path.join(full_path, dir_file)
      size = os.path.getsize(dir_file_path)
      is_file = os.path.isfile(dir_file_path)
      list_dirs.append(f' - {dir_file}: file_size={size}, is_dir={not is_file}')

    return "\n".join(list_dirs)

  except Exception as e:
    print(f'Error: {e}')
  