# def fun(a, b):
#     return a + b, a - b, a * b, a / b
#
#
# x, y, z, r = fun(b=8, a=10)
# print(x, y, z, r)
#
#
# def argy(*a):
#     if len(a) == 1:
#         print("One")
#     elif len(a) == 2:
#         print("Two")
#     elif len(a) == 3:
#         print("Three")
#     else:
#         print("Many")
#
#
# argy(1)
# argy(1, 2)
# argy(1, 2, 3)
# argy(1, 2, 3, 4)

def fact(a):
    if a == 1:
        return 1
    return a * fact(a - 1)


def fibo(n):
    a = 0
    b = 1
    c = 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        while (n - 2) > 0:
            c = a + b
            a = b
            b = c
            n -= 1
        return c


def prim(a, b):
    for i in range(a, b + 1):
        flag = 0
        for j in range(1, i + 1):
            if i % j == 0:
                flag += 1
        if flag == 2:
            print(i)


def argyl(*a):
    if len(a) == 1:
        print(fact(a[0]))
    elif len(a) == 2:
        print(fibo(a[1]))
    elif len(a) == 3:
        if a[2] != "prime":
            print("Enter Valid Argument")
            return
        prim(a[0], a[1])


argyl(6)
argyl(1, 7)
argyl(1, 100, "prim")
