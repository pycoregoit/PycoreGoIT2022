"""Lesson 3 practical"""


def modeling(_factor, *_, correction):
    pass


def modeling_two(factor, _):
    pass


def __hello():
    pass


def hello():
    print("Hello")


def name(name, hello):
    h = hello()
    print(name, hello)


name("alisa", hello())


def count_items(item_list):
    """Recursion function count items in list."""
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count


print(count_items([1, 2, 3, 4]))
print(count_items([1, [2, 3], 4]))
print(count_items([]))


# hello
# civic

def is_palindrome(word: str):
    """Return True if word is Palindrome."""
    return word == word[::-1]


print(is_palindrome("civic"))


# F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 10

for n in range(number):
    print(fibonacci(n))


def greet_users(names: list):
    for name in names:
        msg = "Hello, " + name.title()
        print(msg)


user_names = ["alisa", "bob", "mike"]

greet_users(user_names)


def create_formatted_name(firs_name: str, last_name: str) -> str:
    full_name = firs_name + " " + last_name
    return full_name.title()


while True:
    print("Please enter your name: ")
    print("(enter 'q' if you want to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = create_formatted_name(firs_name=f_name, last_name=l_name)
    print("Hello, " + formatted_name)
