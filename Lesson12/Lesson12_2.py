import pickle


class Computer:
    def __init__(self, name, proc, hdd, ram, cost):
        self.name = name
        self.proc = proc
        self.hdd = hdd
        self.ram = ram
        self.cost = cost

    def details(self):
        print("COMPUTER")
        print(f"Name {self.name}")
        print(f"Proc {self.proc}")
        print(f"HDD {self.hdd}")
        print(f"RAM {self.ram}")
        print(f"COST {self.cost}")


pc = Computer("Lenovo", "Inter core i7", 1028, 32, 1000)

# serialize_file = open("pc.txt", "wb")
# pickle.dump(pc, serialize_file)
# serialize_file.close()

deserialize_file = open("pc.txt", "rb")
type_pc = pickle.load(deserialize_file)
deserialize_file.close()
print(type(type_pc))


class Animal:
    def __init__(self, name, vyd):
        self.name = name
        self.vyd = vyd

leo = Animal("leo", "mammals")

f = open("pick_d", "wb")
pickle.dump(leo, f)
f.close()

f = open("pick_d", "rb")
p = pickle.load(f)
print(p.__dict__)
f.close()

panda = Animal("panda", "bear")
f = open("pick_d", "wb")
pickle.dump([leo, panda], f)
f.close()

f = open("pick_d", "rb")
p = pickle.load(f)
# print(p.__dict__)
f.close()

for a in p:
    print(a.__dict__)


import dill
dill_lib = dill.dumps(lambda x, y: x + y)
print(dill_lib)

# Coppy and deep coppy

n = [1, 2, 3, 4, 5]
c = n
print("===========")
print("n: ", n, "c: ", c)
n.append(6)
print("+++++++++++")
print("n: ", n, "c: ", c)

import copy

n = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6]]
c = n
shallow = copy.copy(n)
deep = copy.deepcopy(n)
n.append(11)
print("===========")
print("n: ", n)
print("shallow: ", shallow)
print("+++++++++++")
print("deep: ", deep)


n = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 6]]
shallow = copy.copy(n)
deep = copy.deepcopy(n)
c = n
# n.append(11)
n[5].append(22)
print("===========")
print("n: ", n)
print("shallow: ", shallow)
print("+++++++++++")
print("deep: ", deep)

d = {"k1": [1, 2, 3], "k2": [4, 5, 6]}
new_d = d.copy()
other_copy = dict(d)
print(d)
print(new_d)
print(other_copy)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point([1, 2], [3, 4])
new_p = p

print(id(p))
print(id(new_p))

p.x[0] = 0
print(new_p.x)

p1 = Point([1, 2], [3, 4])
new_p1 = copy.copy(p1)
print(id(p1))
print(id(new_p1))
p1.x[0] = 0
print(new_p1.x)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.other = [1, 2, 3]

    def __copy__(self):
        p = Point(self.x, self.y)
        p.__dict__.update(self.__dict__)
        p.other = copy.deepcopy(self.other)
        return p

p = Point([1, 2], [3, 4])
new_p = copy.copy(p)

print(id(p))
print(id(new_p))

p.x[0] = 0
p.y[0] = 0
p.other[0] = 0
print(p.x)
print(p.y)
print(p.other)

print("----------------")
print(new_p.x)
print(new_p.y)
print(new_p.other)



class PointDeep:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.other = [1, 2, 3]

    def __deepcopy__(self, memodict={}):
        p = PointDeep(self.x, self.y)
        p.__dict__.update(self.__dict__)
        p.x = copy.deepcopy(self.x, memodict)
        p.y = copy.deepcopy(self.y, memodict)
        return p


p = PointDeep([1, 2], [3, 4])
new_p = copy.deepcopy(p)

print(id(p))
print(id(new_p))

p.x[0] = 0
p.y[0] = 0
p.other[0] = 0
print(p.x)
print(p.y)
print(p.other)

print("----------------")
print(new_p.x)
print(new_p.y)
print(new_p.other)

# JSON

import json

emp = {"name": "Alisa", "job_title": "dev", "lang": "eng"}

f_json = json.dumps(emp, indent=5, separators=(", ", " = "), sort_keys=True)
print(f_json)
