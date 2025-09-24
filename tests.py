# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# result = get_files_content("calculator", "lorem.txt")
# if result:
#   print(result)


result = get_file_content("calculator", "main.py")
if result:
  print(result)

result = get_file_content("calculator", "pkg/calculator.py")
if result:
  print(result)

result = get_file_content("calculator", "/bin/cat")
if result:
  print(result)

result = get_file_content("calculator", "pkg/does_not_exist.py")
if result:
  print(result)