
with open("pi_digits.txt") as file:
  contents = file.read()
  print(contents)


with open("test/test6.txt") as file:
  contents = file.read()
  print(contents)


file_name = "pi_digits.txt"

with open(file_name) as file:
  for line in file:
    print(line)


with open(file_name) as file:
  for line in file:
    print(line.rstrip())


with open(file_name) as file:
  lines = file.readlines()
  for line in lines:
    print(line.rstrip())

with open(file_name) as file:
  lines = file.readlines()
  st_value = ''
  for line in lines:
    st_value += line.rstrip()

print(st_value)
print(len(st_value))


filename = "big_pi.txt"

with open(filename) as file:
  lines = file.readlines()
  pi_number = ''
  for line in lines:
    pi_number += line.rstrip()

  birthday = input("Enter your birthday, format mmddyy: ")
  if birthday in pi_number:
    print("Your birthday in pi numbers")
  else:
    print("Your bithday does not in PI numbers")


filename = "prog_language.txt"

with open(filename, "w") as file:
  file.write("Python, Ruby, C++")


filename = "prog_language2.txt"

with open(filename, "w") as file:
  file.write("Python, Ruby, \n")
  file.write("Java, Go")

filename = "big_text.txt"

try:
  with open(filename) as file:
    content = file.read()
except FileNotFoundError:
  msg = "File " + filename + " not found. "
  print(msg)

else:
  words = content.split()
  num_words = len(words)
  print("This file " + " count " + str(num_words) + " words")


def count_words(filename):
  """Count strings in file."""
  try:
    with open(filename) as file:
      content = file.read()
  except FileNotFoundError:
    msg = "File " + filename + " not found. "
    print(msg)
  
  else:
    words = content.split()
    num_words = len(words)
    print("This file " + " count " + str(num_words) + " words")


filenames = ["big_text.txt", "prog_language.txt", "prog_language2.txt", "test_reverse.txt"]

for file in filenames:
  count_words(file)


# BUFFER

import io
print("Default buffe size: ", io.DEFAULT_BUFFER_SIZE)
with open("big_text.txt", mode="r", buffering=5) as file:
  print(file.line_buffering)
  file_content = file.buffer
  for line in file_content:
    print(line)
  

file = open("big_text.txt", mode="r", errors="stict")

# stricts == ValueErrorException

file = open("big_text.txt", mode="r", newline=None)
print(file.read())
file.close()

# Encoding

with open("big_text.txt") as file:
  print("Default encoding: ", file.encoding)

with open("big_text.txt", encoding="utf-8") as file:
  print("New encoding ", file.encoding)

import os

os.makedir()

