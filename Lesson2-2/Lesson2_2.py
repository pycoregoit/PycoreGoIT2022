"""Lesson2 practical"""

# Try Except
# Handling Error
x = 2
y = 0
try:
    result = x / y
    print(f"Result is equal {result}")
except ZeroDivisionError:
    print("You canno't dive to zero")
else:
    print("All is ok")
finally:
    print("It's finally block")


# For Loop

people = ["alisa", "bob", "mike", "carolina"]
print("People ", people[0][1])
for human in people:
    print("Human", human)

for human in people:
    print(human.title() + ", you are great person")

for value in range(11, 1):
    print("Value ", value)

squares = []

for value in range(11, 11):
    square = value**2
    squares.append(square)

print("Squares ", squares)


cars = ["bmw", "seat", "audi"]
for car in cars:
    if car == "bmw":
        print("Car upper", car.upper())
    else:
        print("Car title", car.title())

request_topping = "pineapple"
if request_topping != "apple":
    print("You got prize")

request_topping = ["mushrooms", "tomatos", "pizza"]
if "mushrooms" in request_topping:
    print("Yes")

word = "Dmytro"
for w in word:
    if "m" in w:
        print("Hello")


available_toppings = ["mushrooms", "olives", "peppers", "papperoni"]

requested_topings = ["mushrooms", "cheese", "tomatos"]

for requested_toping in requested_topings:
    if requested_toping in available_toppings:
        print("Added " + requested_toping)
    else:
        print("Sorry " + requested_toping)


favorite_languages = {
    "dmytro": "python",
    "natali": "c",
    "denys": "ruby",
    "nataly": "python"
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

for language in favorite_languages.values():
    print(language .title() + " Language ")



favorite_languages = {
    "dmytro": ["python", "ruby"],
    "natali": ["c", "c++"],
    "denys": ["ruby"],
    "nataly": ["python", "go"]
}

for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language are ")
    for language in languages:
        print(" " + language.title())

users = {
    "boby": {
        "first_name": "Bob",
        "last_name": "File",
        "location": "Las-Vegas"
    },
    "alisa": {
        "first_name": "Alisa",
        "last_name": "Erickson",
        "location": "New-York"
    }
}

for username, user_info in users.items():
    print("Username " + username)
    full_name = user_info["first_name"] + " " + user_info["last_name"]
    location = user_info["location"]
    print("Full name: " + full_name)
    print("Location: ", location)

# While

current_number = 1

while current_number <= 6:
    print(current_number)
    current_number += 1

message = "Tell something I will repeate:"
message += "Enter 'quit' for end"
promt = ""

while promt != "quit":
    promt = input(message)
    print(promt)

promt = "Please enter the name of city  you would have visited "
promt += "For end please input 'quit' "

while True:
    city = input(promt)
    if city == 'quit':
        break
    else:
        print("I would love to go to " + city.title())

word = "Restaurant"
for w in word:
    if w == "u":
        continue
    print(w)

names = ["alisa", "bob", "mikle"]

for name in names:
    if name == "bob":
        break
    print("All company done")