""" STRINGS """

s = "some string "
n = "new string"

res_string = s + " " + n
print(res_string)

res_str = s * 5
print(res_str)

res_str = s * -5
print(res_str)

res_str = "s" in s
print(res_str)


res_str = "abc" not in s
print(res_str)

value = ord("s")
value2 = ord("S")
print(value)
print(value2)

value_utf = ord("$")
print(value_utf)

value = chr(115)
print(value)


s = "My name is Alisa"
print(len(s))

n = 4
print(type(n))
s = str(n)
print(type(s))

s = "somestring"
print(s[5])
print(s[-1])
print(s[len(s)-1])
print(s[3:7])
print(id(s))

s = "string"
print("S ", s)

name = "Alisa"
surname = "Simpson"
print(f"My name is \" {name}, {surname}")
print("My name is {name}, {surname}".format(name=name, surname=surname))

number = 313.493843294893
print("number: {:0.5}".format(number))


s = "foobar"
res = s.replace("b", "c")
print(res)

s = "foo bar baz"
res_str = s.capitalize()
print(res_str)


s = "Foo@GMAil.com"
res = s.lower()
print(res)

s2 = "Foo@GMAil.com"
res2 = s2.casefold()
print(res2)

s = "foo bar baz"
res_str = s.title()
print(res_str)

s = "foo bar baz"
res_str = s.upper()
print(res_str)


s = "foo bar baz"
res_str = s.count("o")
print(res_str)

s = "foobarbaz"
res_str = s.endswith("baz")
print(res_str)


s = "foo bar baz"
res_str = s.find("bar")
print(res_str)

s.isalpha()
s.isdigit()
s.isalnum()


name = " Alisa  "
n = "Alisa"
print(n == name)

res = name.strip()
print(res == n)

http = "https://www.google.com"
print(http.lstrip("//:https"))

l = ["foo", "bar", "baz", "abc"]

res = ", ".join(l)
print(res)


http = "www.google.com"
res = http.split(".")
print(res)

s = "foo...bar"
res = s.rsplit()
print(res)

s = "foo\t\tbar"
res = s.rsplit()
print(res)

print("My\n nam\re is\t Alisa\r\n, I'm developer")

res = bytes(s, "utf-8")
l = [1, 2, 3, 4]
res = bytes(s, "utf-8")
res_l = bytes(l)

print(res)

print(res_l)


# Regular expressions
# regex

reg = r'[a-z][C-Z][0-9]\@$%'

import re

s = "foobar1234"
print(re.search("1234", s))

x = re.search("[^0-9][0-9][0-9]", s)
print(x)



