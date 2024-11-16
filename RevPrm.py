n = int(input("Enter Number: "))
sum = 0
c = 0
while n > 0:
    num = int(input("Enter Numbers: "))
    sum = sum + num
    c = c + 1
    n-=1
avg = sum / c
print(sum)
print(avg)
