"""Practical Lists, sets, tuples, dicts"""

# SETS

x1 = {"boor", "baz", "foo"}
x2 = {"alisa", "xx", "baz"}
x3 = frozenset(["bob", "mike", "leo"])
print("Type x3", type(x3))
print(x3.add("pizza"))

print(x1.union(x2))


print(x1.intersection(x2))

print(x1.difference(x2))

# LISTS

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

expected = ["My", "name", "is", "Kelly"]

list3 = [l1 + l2 for l1, l2 in zip(list1, list2)]
print("L3 ", list3)


numbers = [1, 2, 3, 4, 5]
expected = [1, 4, 9, 16, 25]

res = []
for n in numbers:
    res.append(n * n)
print(res)


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# 10 400
# 20 300
# 30 200
# 40 100

for l1, l2 in zip(list1, list2[::-1]):
    print(l1, l2)


list1 = ["Mike", "Alisa", "", "Bob", ""]
res = list(filter(None, list1))
print("RES ", res)


# DICTS

employee_dict = {
    "dev": {"name": "Alisa", "salary": 1000},
    "qa": {"name": "Bob", "salary": 1200}
}

employee_dict["dev"]["salary"] = 1200

print("EMP DICT ", employee_dict)


dict1 = {
    "Alisa": 1200,
    "Bob": 1000,
    "Mike": 500
}

print(min(dict1, key=dict1))


emp_location = {
    "name": "Alisa",
    "age": 24,
    "salary": 1200,
    "city": "New York"
}

emp_location['location'] = emp_location.pop("city")
print("EMP LOCATION ", emp_location)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70, 50}

set1.intersection_update(set2)
print(set1)

# TUPLES
t1 = (1, 2)
t2 = (3, 4)

t1, t2 = t2, t1

print(t2)
print(t1)
