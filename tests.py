from functions.run_python_file import run_python_file

result = run_python_file("calculator", "main.py")
if result:
  print(result)

result = run_python_file("calculator", "main.py", ["3 + 5"])
if result:
  print(result)

result = run_python_file("calculator", "tests.py")
if result:
  print(result)

result = run_python_file("calculator", "../main.py")
if result:
  print(result)

result = run_python_file("calculator", "nonexistent.py")
if result:
  print(result)

result = run_python_file("calculator", "lorem.txt")
if result:
  print(result)
