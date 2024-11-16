def binary(dec):
    if dec > 1:
        binary(dec // 2)
    print(dec % 2, end='')


dec = int(input("Enter Decimal Number: "))
binary(dec)
