ch = 'y'
while ch == 'y':
    o = input("Enter Operation: ")
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    if o == "+":
        print(a + b)
    elif o == "-":
        print(a - b)
    elif o == "*":
        print(a * b)
    elif o == "/":
        print(a // b)
    else:
        print("Invalid Operator")
    print("To Continue Press Y")
    ch = input("Enter Choice: ")
    if ch != "y":
        break
print("!Thank You For Using Our Service!")
