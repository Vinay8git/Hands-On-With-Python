st = input("Enter String")
l = len(st)
str = ""
for i in range(l):
    if (not (st[i].isalnum())):
        continue
    else:
        str = str + st[i];
print(str)
