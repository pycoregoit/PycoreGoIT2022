"""Lesson 1-2. Exercises"""

# Input number
number = input("Please input your number: ")
print("You enter: ", number)

# F - strings
number = input("Please input your number: ")
print(f"Your number is {number}")

# print parameters
name = "Alisa"
surname = "Nickols"

print(name, surname, sep=":", end="...")

# Create company email
name = input("Please input your name: ")
surname = input("Please input your surname: ")
print(name, surname, sep="", end="@gmail.com")


# гіпотенуза прямокутного трикутника
x = float(input("Введіть перший катет: "))
y = float(input("Введіть другий катет: "))
hypotenuse = (x ** 2 + y ** 2) ** 0.5
square = x * y / 2

print(f"Hypotenuse is equal: {hypotenuse}")
print(f"Square of triangle is equal: {square}")



print("My", "is", "Oleksandr", sep="**")


number = float(input("Please input your number: "))
result = 4 * number ** 4 - 5 * number
print("Is equal: ", result)

# String exercise
word = "James"
print("Original text is", word)
first = word[0]

len_of_str = len(word)

middle = int(len_of_str / 2)

letter_middle = word[2]

first_plus_second = first + word[middle]

last_symbol = word[-1]


print("First ", first)
print("Length ", len_of_str)
print("Middle ", middle)
print("First Plus Second ", first_plus_second)
print("Last Symbol ", last_symbol)

print("Equal 50", word * 50)

# Calculator of seconds
number = int(input("Введіть кількість секунд "))
hours = number // (60 * 60)
minutes = (number - hours * 60 * 60) // 60
seconds = number - hours * 60 * 60 - minutes * 60

print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")

# What is year century
year = int(input("Введіть рік "))
century = (year - 1) // 100 + 1

print("Ваш рік це століття: ", century)