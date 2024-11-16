class smallval(Exception):
    def __init__(self, arg):
        self.args = arg


class bigval(Exception):
    def __init__(self, arg):
        self.args = arg


try:
    a = int(input("Enter A Number"))
    if a < 10:
        raise smallval("Value Is Small")
    elif a > 10:
        raise bigval("Value Is Big")
    else:
        print("Yes This Is Valid")
except smallval as ex:
    print(type(ex.args))
    for i in ex.args:
        print(i, end=" ")
    print("\n")
except bigval as ex:
    print(type(ex.args))
    for i in ex.args:
        print(i, end="")
    print("\n")
