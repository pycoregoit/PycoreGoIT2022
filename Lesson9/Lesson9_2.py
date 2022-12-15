
import time


def slow_func(func):
  def wrapper(*args, **kwargs):
    time.sleep(2)
    return func(*args, **kwargs)
  return wrapper


@slow_func
def countdown(number):
  if number < 1:
    print("Less the one")
  else:
    print(number)
    countdown(number - 1)

print(countdown(5))


def repeat(num):
  def decorator_repeat(func):
    def wrapper(*args, **kwargs):
      for _ in range(num):
        res = func(*args, **kwargs)
      return res
    return wrapper
  return decorator_repeat


@slow_func
@repeat(num=3)
def greeting(name):
  print(f"Hello {name}")


greeting("Denys")


import random

PLUGINS = dict()

def register(func):
  PLUGINS[func.__name__] = func
  return func

@register
def greeting(name):
  return f"Hello {name}"

@register
def good_bye(name):
  return f"Good bye {name}"


def radom_greet_bye(name):
  greeter, byer = random.choice(list(PLUGINS.items()))
  print(f"Now {greeter}")
  return byer(name)

radom_greet_bye("Alisa")
print(PLUGINS)


import time


def slow_func(func=None, *args, stop=1):
  def dec_slow_func(func):
    def wrapper(*args, **kwargs):
      time.sleep(stop)
      return func(*args, **kwargs)
    return wrapper
  return dec_slow_func

  if func is None:
    return dec_slow_func
  else:
    return dec_slow_func(func)

@slow_func(stop=5)
def countdown(number):
  if number < 1:
    print("Less the one")
  else:
    print(number)
    countdown(number - 1)

countdown(5)


# MAP

x = list(map(lambda l: l.capitalize(), ["alisa", "bob", "mike"]))
print(x)

c = [l.capitalize() for l in ["alisa", "bob", "mike"]]
print(c)

even = lambda n: n % 2 == 0
e = list(filter(even, range(20)))
print(e)
e_l = [e for e in range(20) if e % 2 == 0]
print(e_l)


s = [1.12345, 2.12345, 3.12345, 44.12345, 55.12345]

res = list(map(round, s, range(1, 7)))
print(res)

round(1.12345, 1)

# zip

empl = ["alisa", "bob", "mike", "ann"]
salary = ["100", "200", "300", "400"]

res = list(zip(empl, salary))
print("ZIP ", res)


empl_m = ["alisa", "bob", "mike", "ann"]
salary_m = ["100", "200", "300", "400"]

res_m = list(map(lambda e, s: (e,s), empl_m, salary_m))
print("MAP ", res_m)


pal = ("tenet", "civic", "madam", "kino", "auto")

res = list(filter(lambda w: w == w[::-1], pal))

print(res)


books = [
  {"Title": "Time", "Author": "Brown", "Price": 200},
  {"Title": "Kobzar", "Author": "Shevchenko", "Price": 300},
  {"Title": "Zapysky", "Author": "Kostenkp", "Price": 500}
]

def book_func(books: list):
  if books["Price"] > 200:
    return True
  else:
    return False

filter_obj = filter(book_func, books)
print(filter_obj)
for b in filter_obj:
  print(dict(b)["Title"])