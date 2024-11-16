x = (i for i in range(3))  # Generator

for i in x:
    print(i)
for i in x:  # Bcz once generator is exhausted it is empty can not perform anything
    print(i)

print(type(x))
print(type(i))

# def ef():
#     a=1
#     return a
#
# a=ef()
# print(next(a))         TypeError: 'int' object is not an iterator

list1 = list()
print(type(list1))
list2 = []

num = [1, 2, 3, 4]
num.append([5, 6, 7, 8])
print(num)
num.extend([5, 6, 7, 8])
print(num)
