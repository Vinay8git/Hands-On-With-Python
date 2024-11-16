def fun(a):

    if(a==0):

        return 0

    return a*fun(a-1)

print(fun(-3))