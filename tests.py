# from functions.get_files_info import get_files_info
from functions.write_file import write_file

# result = get_files_content("calculator", "lorem.txt")
# if result:
#   print(result)


result = write_file("calculator", "lorem2.txt", "wait, this isn't lorem ipsum")
if result:
  print(result)

result = write_file("calculator", "test/morelorem.txt", "lorem ipsum dolor sit amet")
if result:
  print(result)

result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
if result:
  print(result)


# result = get_file_content("calculator", "main.py")
# if result:
#   print(result)

# result = get_file_content("calculator", "pkg/calculator.py")
# if result:
#   print(result)

# result = get_file_content("calculator", "/bin/cat")
# if result:
#   print(result)

# result = get_file_content("calculator", "pkg/does_not_exist.py")
# if result:
#   print(result)