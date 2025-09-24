from functions.get_files_info import get_files_info

result = get_files_info("calculator", ".")
if result:
  print(result)

result = get_files_info("calculator", "pkg")
if result:
  print(result)

result = get_files_info("calculator", "/bin")
if result:
  print(result)

result = get_files_info("calculator", "../")
if result:
  print(result)