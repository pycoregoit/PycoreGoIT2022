"""Lesson 2-1 Loops, conditions"""

age = input("How old are you? ")

#If condition
if age >= 18:
    print(f"Your age is {age} is more than 18 you can continue use the web site")
else:
    print("You canno't use the web site")

# Debugger
if type(age) is int:
    if int(age) >= 18:
        print(f"Your age is {age} is more than 18 you can continue use the web site")
    else:
        print("You canno't use the web site")
else:
    print("It is not a int type")

# Ternary operator
number = 7
message = "Even" if number % 2 == 0 else "Odd"
print(message)

number = 8
message = ""

if number % 2 == 0:
    print("Even")
elif number % 2 != 0:
    print("Odd")
else:
    print("Not number")


your_age = input("Please enter your age ")
driving_license = "Yes, you can drive car" if int(your_age) >= 18 else "Sorry(( "
print(driving_license)

number = input("Please enter your number ")
number = int(number)

if number > 0:
    print("It's positive number")
elif number < 0:
    print("It's negative number")
else:
    print("This number is zero")

result = None
if result:
    print(result)
else:
    print("Result is None")

user_email = input("Please enter your email ")

if user_email:
    print(f"Your emails is {user_email}")

else:
    print("You forgot about your email")

# While loop

number = 1
while number <= 5:
    print(number)
    number += 2

# break
number = 0
while True:
    print(number)
    if number >= 10:
        break
    number += 1

while True:
    user_exit = input().lower()
    print(user_exit)
    if user_exit == "exit":
        break


# Continue
number = 0
while number <= 10:
    number += 1
    if not number % 2:
        continue
    print(number)


unconfirmed_users = ["alisa", "bob", "mike"]

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verified users: " + current_user.title())


# FOR loop

name = "Alisa is a greate girl"
for letter in name:
    print(letter)

# list loop
list_of_fruits = ["apple", "orange", "tangirene"]
for fruit in list_of_fruits[1]:
    print(fruit)

# dict loop
student = {"name": "Bob", "age": 20}
for key, value in student.items():
    print("KEY ", key)
    print("VALUE ", value)