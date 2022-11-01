""" FUNCTIONS """
import math

def greeting():
    print("Hello!")


def greeting(name):
    print(f"Hello {name}")


def greeting(last_name, first_name):
    return f"Hello {first_name} {last_name}"


print(greeting(first_name="Alisa", last_name="Simpson"))


def person(first_name: str, last_name: str, age: int, profile="developer") -> str:
    """This function about person
    fisrt_name: it's person name, type string
    :return string
    """
    return f"Hello {first_name} {last_name}, you are {age} year's old, you are {profile}"


print(person("Alisa", "Simpson", 22, "QA"))

# LEGB
t = 5
c = 7

def calc(x=2, y=3):
    x = 7
    y = 10
    return x + y

print(calc())

def calc(func):
    y = "B"
    def greet():
        x = "A"
        print("Hello", x, y, t, math.sqrt(10))

name = "Bob"


def greeting():
    global name
    print(f"Hello global {name}")

    name = "Alisa"
    print(f"Helo {name}")

greeting()
print("Name ", name)

# ARGS & KWARGS

def some_func(*args):
    for arg in args:
        print(arg)


some_func("Hello", "Alisa", "you", "are", "developer", 4, 5)

def dict_func(**kwargs):
    for key, value in kwargs.items():
        print("Key: ", key, "Value: ", value)

dict_func(firs_name="alisa", second_name="simpson", age=20)


def super_function(param1: int, param2: int, *args, **kwargs) -> None:
    print(f"param1 = {param1}")
    print(f"param2 = {param2}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")


super_function(3, 5, "alisa", "developer", age=20, salary=1000, location="New-York")


def function_one():
    s = "Hello"

    def function_two():
        print(s)

    function_two()


function_one()

# Recursion

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(12))

# RecursionError
def function():
    x = 5
    function()

function()

def countdown(n):
    print(f"Countdown {n}")
    if n == 0:
        return
    else:
        countdown(n - 1)

countdown(10)
