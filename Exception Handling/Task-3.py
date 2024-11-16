# furniture = {"Table": 1000, "Chair": 500, "Cupboard": 2500, "Bed": 5000, "Basin": 1200}
# try:
#     frntr = input("Enter Furniture You Want To Buy")
#     print(furniture[frntr])
# except Exception as e:
#     print("Error")
def fun():
    try:
        n = int(input("Enter Number   "))
    except Exception as err:
        print(err)
    finally:
        print("Want to continue")
        ch = input("Enter y/n")
        if ch == 'y':
            fun()


fun()
