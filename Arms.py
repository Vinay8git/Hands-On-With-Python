import math

n = int(input("Enter Number"))
c, z = 0, n
sum = 0
while z > 0:
    z = z // 10
    c = c + 1
z = n
while n > 0:
    dig = n % 10
    power = int(math.pow(dig, c))
    sum = sum + power
    n = n // 10
if sum == z:
    print("Armstrong")
else:
    print("Not Armstrong")
