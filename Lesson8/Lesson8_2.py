
from collections import defaultdict
import random

new = defaultdict(str)

new[1] = "White"
new[2] = 'Black'
new[3] = "Blue"


for n in range(1,10):
  print(new[n])


new = defaultdict(str)
list_of_colors = ["Red", "Yellow", "Orange", "Green"]

new[1] = "White"
new[2] = 'Black'
new[3] = "Blue"


for key in range(0,7):
  if new[key] == "":
    new[key] = list_of_colors[random.randint(0,3)]

print(new)


from collections import namedtuple

person = namedtuple("person", "name, job, age")

person1 = person("Alisa", "Developer", "25")

print("Detail of person1: ", person1)
print("Person's 1 job ", person1.job)
print(type(person1))

from collections import Counter

c = Counter("The yellow yellow list")

print(c)

animals = Counter(("Dog", "Turtle", "Panda"))
animals["Dog"] = 0
print(animals)
del animals["Dog"]
print(animals)


from collections import ChainMap

first = {"fruit": "apple", "vegatable": "potato"}
second = {"color": "blue", "car": "volvo"}
third = {"name": "alisa", "surname": "simpson"}

new_map = ChainMap(first, second, third)
print(new_map)


fourth = {"job": "developer"}

new_map.new_child(fourth)

print("New ChainMap ", new_map)


# IANA
from dateutil import tz
from datetime import datetime

# now = datetime.now(tz=tz.tzlocal())
# print(now)
# print("Name of time zome ", now.tzname())


London_tz = tz.gettz("Europe/London")
now1 = datetime.now(tz=London_tz)
print(now1)
print("Name1 of time zome ", now1.tzname())


from dateutil import parser, tz
from datetime import datetime

new_date = parser.parse("December 07, 2022 8:25 PM")
new_date = new_date.replace(tzinfo=tz.gettz("America/New_York"))
now = datetime.now(tz=tz.tzlocal())

result = new_date - now

print(f"Time US: {result}")


from calendar import monthrange

m = monthrange(2022, 12)
print(m)


from datetime import datetime, timedelta

now = datetime.now()
print(now)

tommorow = timedelta(days=+1)

# print(now + tommorow)

delta = timedelta(days=+4, hours=-4)

print(now + delta)


from dateutil.relativedelta import relativedelta


delta = relativedelta(years=+3, month=+1, days=+4, hours=+2, minutes=-25)
print("Relative delta ", now + delta)

from datetime import date

date.fromisoformat("2022-12-07")
print(datetime.date)


date_string = "12-07-2022 21:02:00"
format_string = "%m-%d-%Y %H:%M:%S"

import dateparser
dateparser.parse("yesterday")
dateparser.parse("morgen")