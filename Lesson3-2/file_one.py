# import file_two
from file_two import f3, f4

print(f" File one __name__ is set to: {__name__}")


def f1():
    print("Function 1")


def f2():
    print("Function 2")


if __name__ == "__main__":
    print("File one executed when ran directly")
    f2()
    f3()
    f4()
else:
    print("File one executed when imported")



