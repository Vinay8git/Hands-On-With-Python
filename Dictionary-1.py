d = {"name": "JOn Snow", "Age": 25, "Country": "Castle Black"}
d["City"] = "Wall"
print(d)
del d["Age"]
print(d)

for key, val in d.items():
    print(key, val)

d["City"] = "Valerian"
print(d)

d["JOnSnow"] = "kit Har"
print(d)

for key in sorted(d.keys()):
    print(key)

d1 = {"Aamit": 100, "Khonsu": 80, "Steven": 40, "Marc": 60}
print(d1)

for key in sorted(d1.values(), reverse=True):
    print(key)
topr = ""
max = 0
for k, v in d1.items():
    if v > max:
        max = v
        topr = k
print(topr)

for key in sorted(d1.keys()):
    print("%s: %s" % (key, d1[key]))

sortedByValue = sorted(d1.items(), key=lambda x: x[0])
print(sortedByValue)

# print(sortedByValue[1][0])
#
# sortedByValue=sorted(d1.items(),key=lambda x:x[1])
# print(sortedByValue)

# print(sortedByValue[-1][0])

list = list()
ans = 'y'
while ans == 'y':
    d3 = dict()

    d3["name"] = input("Enter Name: ")
    if d3["name"] in list:
        print("Already exists")
        print("Want to enter more data")
        ans = input()
    d3["age"] = input("Enter Age: ")
    list.append(d3)
    ans = input("Want To Enter MOre Data: ")

print(list)
