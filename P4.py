s1 = input("Enter String")
s2 = input("Enter String")
res = ""
l = len(s1) + len(s2)
x, y = 0, 0
for i in range(l):
    if i % 2 == 0:
        res += s1[x]
        x += 1
    else:
        res += s2[y]
        y += 1
print(res)
