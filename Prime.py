import math

n = int(input("Enter Number"))
c = 0
for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        c = 1
        break
if c == 1:
    print("Not Prime")
else:
    print("Prime")
