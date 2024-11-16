# print(reduce(lambda x, y, z: x + y + z, [1, 2, 3, 4]))

# Filter
# fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = filter(lambda x: x % 2 != 0, fib)
# print(list(result))
#
# result = filter(lambda x: x % 2 == 0, fib)
# print(list(result))

# Zip fn takes run along two or more lists from 0 to till they have common length
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [8, 9, 10, 11, 12, 13, 14]
for x, y in zip(l1, l2):
    print(x, y)

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(list(zip(T1, T2, T3)))
