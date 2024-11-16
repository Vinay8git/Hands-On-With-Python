def sum(a, b):
    if a < 0 and b < 0:
        s = 0
        if b == 0:
            return a
        if a == 0:
            return b
        s = s - 2 + sum(a + 1, b + 1)
        return s
    if b == 0:
        return a
    if a == 0:
        return b
    return 2 + sum(a - 1, b - 1)


a = int(input("Enter A : "))
b = int(input("Enter B : "))
print(sum(a, b))
