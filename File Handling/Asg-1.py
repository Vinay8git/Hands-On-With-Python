d = open("D:\\ASG-1.txt", "w")
d.write("My name is Vibhor Sharmeele and I am a member of the topa culture\n")
d.write("My friend name is Vinayak Shukliiiiiii and he is a chapraasi in the topa culture")
d.close()

d = open("D:\\ASG-1.txt", "r")
lines = 1
words = 1
s = d.readlines()
while s:
    lines += 1
    s = d.readline()

print("Number of lines in the file:", lines)
d.seek(0)
st = d.read(1)
while st:
    words += 1
    st = d.read(1)
    if

print("Number of words in the file:", words)
