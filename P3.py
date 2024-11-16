st = input("String: ")
max = 0
s = ""
maxc = ""
for i in range(len(st) - 1):
    c = 0
    for j in range(i + 1, len(st)):
        if (st[i] == st[j]):
            c += 1
            # s=s[i]
    if c > max:
        max = c
        maxc = st[i]
print(maxc + " :" + max)
