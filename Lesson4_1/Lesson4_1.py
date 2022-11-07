"""Lists, sets, tuples, dictionaries"""

l = ["foo", "bar", 1, 2, [4, 5]]
print("LIST L ", l)
print("Type L ", type(l))

l2 = ["alisa", "bob"]

print("Is l equal l2 ", l == l2)

print(l[-4:-2])

print(l[2:], l[0:4])

# start : end : step
print(l[0:4:2])

print(l[0::2])

print(l[::-1])


l = ["foo", "bar", 1, 2, [4, 5]]
print("foo" in l)
print("pass" in l)

l2 = ["alisa", "bob"]
print(l + l2)
print(l*3)
print("Length of lsit l ", len(l))

print(l[4][0])

l[1] = "name"
print(l)

l = ["foo", "bar", 1, 2, [4, 5], "pass"]
l.append("hello")
print(l)
l.extend([6, 7, 8])
print(l)
l.clear()
print("Clear ", l)

l.insert(2, "pass")
print(l)

l.remove("pass")
print(l)

l.pop(-3)
print(l)

l = []
print(type(l))

# TUPLE

t = ()
print(type(t))

t = ("foo", "bar", "baz", "pass")
print(type(t))

t1 = (1, )
print(type(t1))

print(t[::-1])
(v1, v2, v3, v4) = t
print(type(v1))

# Dictionaries

d1 = {
    "name": "alisa",
    "age": 22,
}

d2 = dict(name="bob", age=25)

print("D1 ", d1)
print("D2 ", d2)

print(d1["name"])

d1["location"] = "London"
print("D1 ", d1)

d1.update({"job": "test"})
print("D1 ", d1)

print(len(d1))

d1.clear()
print("D1 ", d1)

print("D1 ", d1.get("job", None))

print("ITEMS ", list(d1.items()))

print(d1.keys())
print(d1.values())

print("D1 ", d1)
d1.popitem()
print("D1 ", d1)


# SET
s = set(["foo", "bar", "baz"])
print("SET ", s)
s = {1, 2, 3, 4}
s.add(5)

print("SET ", s)

s_str = set("foo")

print("SET STR", s_str)

s2 = {4, "foo", None, True, (2, 3)}
print("SET 2", s2)

