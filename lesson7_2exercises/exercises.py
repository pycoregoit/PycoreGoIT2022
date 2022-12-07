# str1 = "London-is-a-capital-of-Great-Britain"
#
# new_str = str1.split("-")
# print("New str ", new_str)
#
# for sub_string in new_str:
#     print(sub_string)

# list1 = ["Alisa", "Bob", "", "Mike", None, "Caroline"]
#
# result_list = []
#
# for l in list1:
#     if l:
#         result_list.append(l)
# print("Result list ", result_list)


# str2 = "Alisa18 is a student in course4 and learn python"
#
# res = []
#
# temp = str2.split()
# print("Temp ", temp)
#
# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)
#
# print("Res ", res)
# for r in res:
#     print(r)

# import string
#
# str3 = "/^Alisa is @python developer & ruby *dev"
#
# replaced_char = "#"
#
# for char in string.punctuation:
#     str3 = str3.replace(char, replaced_char)
#
# print("Str3 ", str3)

new_dict = {
    "name": "Alisa",
    "age": 22,
    "position": "developer",
    "salary": 1000
}

# long variant

keys_extract = ["name", "salary"]

# res_dict = dict()

# for k in keys_extract:
#     res_dict.update({k: new_dict[k]})
#
# print("Result ", res_dict)

# result_dictionary = {k: new_dict[k] for k in keys_extract}
# print("result_dictionary", result_dictionary)


# Recursion

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

print(fib(5))