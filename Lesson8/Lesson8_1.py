
# urllib

from urllib.request import urlopen

# page = urlopen("https://www.google.com.ua/")
page = urlopen("https://www.apple.com/")

content = page.read()

print(page.headers)
print("")
print(content)


# dis

import dis

def greet(name):
  print(f"Hello {name}")


def test(number):
  return (str(number) + str(number))

dis.dis(greet)

dis.dis(test(2))


# pip instal emoji

from emoji import emojize

print(emojize(":thumbs_up:"))


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

point = Point(2, 5)

print("point ", point)

print("point x ", point.x)
print("point y ", point.y)
print("point inx ", point[0])

generator expression
Point = namedtuple("Point", (field for field in ["apple", "orange"] ))
print(Point(2, 5))

Human = namedtuple("Employee", "name position", defaults=["Python developer"])

human = Human("Alisa", "Ruby")
print(human)

print(human._asdict())

human = human._replace(position="Ruby Developer")
print(human)

# O(n)
# O(1)
# deque


from collections import deque

ticket_queue = deque()
print(ticket_queue)

ticket_queue.append("Alisa")
ticket_queue.append("Bob")
ticket_queue.append("Dmytro")

print(ticket_queue)

one = ticket_queue.popleft()
print(one)
two = ticket_queue.popleft()
print(two)
three = ticket_queue.popleft()
print(three)
extra = ticket_queue.popleft()
print(extra)


recent_pages = deque(["main_page", "shop", "order"], maxlen=3)

recent_pages.appendleft("cart")
print(recent_pages)

recent_pages.appendleft("login")
print(recent_pages)


from collections import OrderedDict

employees = OrderedDict()

employees["developer"] = "1000-2000"
employees["qa"] = "500-1000"
employees["pm"] = "1500-2500"
employees["ba"] = "2000+"

for empl, salary in employees.items():
  print(empl, "->", salary)



# [1, 2, 3, 4, 5]

letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters)
letters.move_to_end("b")
print(letters)

cart = {"toys": "cars", "color": "orange"}

# print(cart["items"])
print(cart.get("items", 2))

# cart.setdefault("items", "2")
print(cart)


from collections import defaultdict

cars = defaultdict(int)

# print(cars)

cars["mercedes"]
print(cars)

cars["mercedes"] +=1
cars["audi"] +=1
cars["mercedes"] +=1
cars["audi"] +=1
cars["mercedes"] +=1


print(cars)


cars = [
  ("mercedes", "s600"),
  ("mercedes", "G"),
  ("mercedes", "A"),
  ("audi", "a100"),
  ("audi", "a8")
]


cars_sallon = defaultdict(list)

for car, model in cars:
  cars_sallon[car].append(model)

print(cars_sallon)


from collections import ChainMap

cmd_proxy = {} # User doesn't provide a proxy
dev_proxy = {"proxy": "proxy.dev.com"}
prod_proxy = {"proxy": "proxy.prod.com"}

configuration = ChainMap(cmd_proxy, dev_proxy, prod_proxy)
configuration["proxy"]

print(configuration)