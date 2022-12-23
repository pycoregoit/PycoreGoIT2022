# UserString

# 'aBcD'

from collections import UserString
import re

class OurClass(UserString):
  def __init__(self, string):
    self.data = re.sub(r'[^\w\s]', '', string)

  def our_string(self):
    s = ''
    for idx in range(len(self.data)):
      if not idx % 2:
        s += self.data[idx].upper()
      else:
        s += self.data[idx].lower()
    print(s)


res_string = OurClass('Hello my name is Alisa')
res_string.our_string()
print(res_string)


class BankAccount:
  def __init__(self, ac_number, cust_name, balance):
    self.ac_number = ac_number
    self.cust_name = cust_name
    self.balance = balance

  def deposite(self, dep):
    self.balance = self.balance + dep

  def withdraw(self, w):
    if self.balance < w:
      print("No money no honey")
    else:
      self.balance = self.balance - w

  def bank_fee(self):
    self.balance = (70/100) * self.balance


  def display(self):
    print("Account number: ", self.ac_number)
    print("Customer name: ", self.cust_name)
    print("Account balance: ", self.balance)


alisa = BankAccount(1234567, "Alisa", 10000)
alisa.withdraw(500)
alisa.deposite(100)
alisa.display()

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def perimeter(self):
    return (self.length + self.width) * 2

  def area(self):
    return self.length * self.width

  def display(self):
    print("Length of rectangle is: ", self.length)
    print("Width of rectangle is: ", self.width)
    print("Perimeter of rectangle is: ", self.perimeter())
    print("Area of rectangle is: ", self.area())


class Parallepiped(Rectangle):
  def __init__(self, length, width, height):
    #super().__init__(self, length, width)
    Rectangle.__init__(self, length, width)
    self.height = height

  def volume(self):
    return self.length * self.width * self.height


rec = Rectangle(5, 4)
rec.display()

parallelepiped = Parallepiped(5, 4, 3)
print("-----------------------")
print("Volume of Paralelepiped is: ", parallelepiped.volume())


class Calculator:
  def __init__(self):
    pass

  def factorial(self, n):
    i = 1
    for k in range(1, n + 1):
      i = i * k
    return i

  def sum(self, n):
    i = 0
    for k in range(1, n + 1):
      i = i + k
    return i

  def test_simpl(self, n):
    j = 0
    for i in range(1, n + 1):
      if n % i == 0:
        j = j + 1
    if j == 2:
      return True
    else:
      return False

  def tes_two_simpl(self, n, m):
    div = 0
    for i in range(1, n + 1):
      if n % i == 0 and m % i == 0:
        div += 1
      if div == 1:
        print(f"Numbers {n} and {m} are co-simple")
      else:
        print(f"Numbers {n} and {m} are not co-simple")

  def mult(self, k):
    for i in range(1, 10):
      print(f"{i} x {k} = {i * k}")

  def list_div(self, n):
    l_div = []
    for i in range(1, n + 1):
      if n % i == 0:
        l_div.append(i)
    return l_div

calculator = Calculator()

print(calculator.factorial(5))
print(calculator.list_div(10))
print(calculator.sum(1))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Human name {self.name}")
        print(f"Human age {self.age}")


class Employee(Human):
    def __init__(self, name, age, position):
        Human.__init__(self, name, age)
        self.position = position

    def emp_disp(self):
        print(f"Emp name {self.name}")
        print(f"Emp age {self.age}")
        print(f"Emp age {self.position}")


human = Human("Alisa", 28)
human.display()
print("----------------------")

employee = Employee("Bob", 30, "dev")
employee.display()
employee.emp_disp()