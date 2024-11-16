# 1
def check_value(meassage, num):
    msg = meassage[:num]
    return len(msg)


result = check_value("Infosys", 4)
print(result)

# 2.

list1 = [1, 2, 3, 4]
print(list1[3])
# print(list1[4])    Index Out Of Bounds Error
# print(list1[5])

# 3.

list1.pop(0)  # Pops last element if no parameter is passed in pop() fn. Else if passed, pop Indexed element
print(list1)

#4.

list2=[10,10,10,10,10,10]
for i in list2:
    list2.remove(i) #In case of for loop, it is dependent only on the locations but while is dependant on the values
print(list2)

#5.
list3=[10,10,10,10,10,10]
while i in list3:
    list3.remove(i)
print(list3)

#6.
list4=[10,10,10,10,10,10]
for i in list4[:]:

    list4.remove(i)
    # i-=1
print(list4)

#7.
