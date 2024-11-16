# # Normal Red Termination
# a = int(input("Enter Number: "))
# b = int(input("Enter Number: "))
# c = a // b
# print(c)
# #Exception Handling Termination
# try:
#     a = int(input("Enter Number: "))
#     b = int(input("Enter Number: "))
#     c = a // b
#     print(c)
# except:
#     print("Error: Divisor Is Zero: Answer-Infinite")
# try:
#     a = int(input("Enter Number: "))
#     b = int(input("Enter Number: "))
#     c = a / b
#     print(c)
#     lt=[1,2,3,4,5,6,7,8,9]
#     print(lt[100])
# except Exception as e:
#     print("Error: ", e)
try:
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    c = a / b
    print(c)
    lt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lt[100])
except Exception as e:
    print("Error: ", e)
finally:
    print("Running Successfully")
