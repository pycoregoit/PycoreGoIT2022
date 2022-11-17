"""Regular expressions"""
import re

text = "The same the new text by Alisa the"

t = re.findall("the", text, flags=re.I)

print(t)


def some_pattern(text):
  return re.findall("the", text, flags=re.I)

print(some_pattern(text))

def search_pattern(text):
  span = re.search("the", text)
  return span.span()

print(search_pattern(text))


t = re.match("the", text)

print(t)


is_match = re.match("the", text, flags=re.I)

if is_match:
  print(f"{is_match.group()} appears at {is_match.span()}")

else:
  print(is_match)


text = "my password is 123456"

change = re.sub("123456", "*", text)

print(change)

text = "Hello, my, name, is! Alisa good developer"
s = re.split(",", text)

print(s)


text = "Hello! We are good devs with_80 level"

pattern = r"\w"

p = re.findall(pattern, text)
print(p)



text = "Hello! We are good devs with_80 level @"

pattern = r"\W"

p = re.findall(pattern, text)
print(p)


pattern = r"\d"

p = re.findall(pattern, text)
print(p)


pattern = r"\D"

p = re.findall(pattern, text)
print(p)


pattern = r"\s"

p = re.findall(pattern, text)
print(p)

pattern = r"\S"

p = re.findall(pattern, text)
print(p)

text = "Hello! We are good devs with_80 level @"

pattern = r"[a-fA-F]"

p = re.findall(pattern, text)
print(p)


pattern = r"[^a-fA-F]"

p = re.findall(pattern, text)
print(p)


text = "hello hello ago gelloo helloooooofdfdrfr hell"

pattern = r"hello+"

p = re.findall(pattern, text)
print(p)

pattern = r"hello*"

p = re.findall(pattern, text)
print(p)


pattern = r"hello?"

p = re.findall(pattern, text)
print(p)


text = "10.55% taxes in 2022 and in 2023 will be incresead. 2024"

pattern = r"\d{4}"

p = re.findall(pattern, text)
print(p)

# {min, max}

text = "alisa@gmail.com, bob@mail.us, mike@web.biz"
pattern = r"\.\w{2,5}"

p = re.findall(pattern, text)
print(p)

#{min,}
text = "Hello! We are good devs with_80 level @"

pattern = r"\w{5,}"
p = re.findall(pattern, text)
print(p)


text = "100 000 items"

pattern = r"^\d\d"
p = re.findall(pattern, text)
print(p)

# Groups
text = "Ilona work on phone"

pattern = r"(.o.)"
p = re.findall(pattern, text)
print(p)


text = "Ths @alisa email alisa@gmail.com"

pattern = r"(\w+)@(\w+)\.(\w+)\b"
p = re.search(pattern, text)
print(p)

print(p.group(0))
print(p.group(1))
print(p.group(2))
print(p.group(3))


