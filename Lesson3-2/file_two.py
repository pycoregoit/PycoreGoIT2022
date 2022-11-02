
print(f" File two __name__ is set to: {__name__}")


def f3():
    print("Function 3")


def f4():
    print("Function 4")


if __name__ == "__main__":
    print("File one executed when ran directly")
else:
    print("File one execited when imported")