# Python Serialization

# pickle

# PICKLE = 4

import pickle
name = "Alisa"
f = open("file.txt", "r+b")
pickle.dump(name, f)

print(pickle.dumps(name))

f.seek(0)
print(pickle.load(f))


class PickleExample:
    name = "Alisa"
    age = 25
    lang = ["eng", "span"]
    offices = {"first": "New York", "second": 1, "third": [1, 2, 3]}
    floors = (5, 8)

pickle_example = PickleExample()
pickled = pickle.dumps(pickle_example)
print("Pickled object: ", pickled)

pickle_example.offices = None

unpickled = pickle.loads(pickled)
print("Unpickled object: ", unpickled.offices)
print("Unpickled object: ", unpickled.floors)


class GetStatePickle:
    def __init__(self):
        self.num = 25
        self.string = "hello"
        self.func = lambda x: x * x

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes["func"]
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.func = lambda x: x * x

ex = GetStatePickle()
pickle_str = pickle.dumps(ex)
pickle_instance = pickle.loads(pickle_str)

print(pickle_instance.__dict__)

# JSON

{
    "name": "Alisa",
    "age": 25
}

import json
list_1 = [1, 2, 3, "name", "age"]
print(type(list_1))
list_1_dumps = json.dumps(list_1)
print(type(list_1_dumps))
print(list_1_dumps)


from json import JSONEncoder


class Car:
    def __init__(self, efficiency, fuel):
        self.efficiency = efficiency
        self.fuel = fuel

    def drive(self, distance):
        max_dist = self.fuel * self.efficiency

        if distance > max_dist:
            print(f"Travel {max_dist} out of fuel")
            self.fuel = 0

        else:
            self.fuel -= distance / self.efficiency
            print("Arriving is good")


class CatJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

car_d = Car(8, 100)
car_d.drive(50)
print(car_d.fuel)

car_serial = json.dumps(car_d, cls=CatJSONEncoder)
print(car_serial)
print(type(car_serial))

import json
n = None
s = json.dumps(n)
print(s)

t = True
s_t = json.dumps(t)
print(s_t)

students = {1: "alisa", 2: "bob"}
st_js = json.dumps(students)
print(st_js)


# (SHALLOW)COPY AND DEEP COPY

import copy

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_l = copy.copy(l)
print(new_l)
print(id(l), id(new_l))
print(id(l[0]), id(new_l[0]))


l_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_l_d = copy.deepcopy(l)

print(new_l_d)
print(id(l_d), id(new_l_d))
print(id(l_d[0]), id(new_l_d[0]))
