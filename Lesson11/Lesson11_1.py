# Magic methods or dunder methods

class Employee:
    # def __new__(cls, *args, **kwargs):
    #     pass

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

alisa = Employee(name="Alisa", age=25, role="developer")

# __new__(cls, other)
# __init__(self, other)
# __del__(self)


class Car:
    pass


class Vehicle(object):
    pass


car = Car()
vehicle = Vehicle()

print(car, vehicle, sep="\n")

class Vehicle:
    def __repr__(self):
        return f"{self.__class__.__qualname__}"

vehicle = Vehicle()
print(vehicle)

class Vehicle:
    def __str__(self):
        return f"{self.__class__.__qualname__}"

vehicle = Vehicle()
print(vehicle)

# __unicode__(self)
# __hash__(self)
# __nonzero__(self)


class String:
    def __init__(self):
        self.x = 111
        self.y = 12.2

    def __unicode__(self):
        return f"dunder unicode {self.x} {self.y}"

s = String()
print(s.__dict__)

# print(unicode(s))
print(f"{s}")


import string

class Letters:
    def __setattr__(self, key, value):
        self.__dict__[key] = value.upper()

l = Letters()

l.letters = string.ascii_lowercase
print(l.letters)


class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Math):
            return NotImplementedError
        return Math(other.x + self.x, other.y + self.y)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplementedError
        return Math(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.x}, {self.y})"


res1 = Math(2, 4)
res2 = Math(5, 9)

print(res1 + res2)

m = Math(2, 4)
print(m * 5)
print(10 * m)

class People:
    def __init__(self, id, name, positions=[], locations={}):
        self.id = id
        self.name = name
        self.positions = positions
        self.locations = locations

    def __delattr__(self, item):
        print("Deletion of attribute " + item)
        return object.__delattr__(self, item)

p = People(11, "Alisa", ["dev", "lead"], {"Kyiv": "Pechersk", "Lviv": "Center"})

print(dir(p))

del p.name
print(p.name)

class People:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id

    def __len__(self):
        return len(self.name)


p1 = People(11, "Alisa")
p2 = People(11, "Bob")
print(p1 == p2)
print(len(p1))


class Point:
    x = None
    y = None

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        print("Method __add__")
        x = self.x + other.x
        y = self.y + other.y

    def __call__(self):
        print(f"class Point called {self.x}, {self.y}")


p1 = Point(2, 4)
p2 = Point(5, 9)
res = (p1 + p2)
p1()
p2()

