# d={1:"A", 2:"B", 3:"C", 4:"D"}
# print(d.get(5,6))

# d={1:"A", 2:"B", 3:"C", 4:"D"}
# print(d.setdefault(5,"E"))
# print(d)

d={1:"A", 2:"B", 3:"C", 4:"D"}
e={1:"a", 2:"b", 3:"c", 4:"D", 5:"E"}
d.update(e)
print(d)