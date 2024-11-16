# #Call by reference
# def run(list1):
#     list1[0]=100
#     print(list1)
#
# list2=[1,2,3,4,5,6,7]
# run(list2)
# print(list2)

#Call by Value
def run(list1):
    list1[0]=100
    print(list1)

list2=[1,2,3,4,5,6,7]
run(list2[:])
print(list2)