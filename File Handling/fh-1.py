d = open(r"D:\\ElitePFH.txt")
# d.write("Hello World")
# d.write("\tHi There")
# s = d.readlines()  # Return type list
# print(type(s))
# print(s)
#
# s = d.readline()  # Return type string
# print(type(s))
# print(s)
#
# s = d.read()  # Return type
# print(type(s))
# print(s)

# print(d.tell())  # Return cursor position
# s=d.read()
# print(d.tell())
# print(s)

# s=d.readline()     #Bcz cursor position has come down
# print(s)
# s=d.readline()
# print(s)

# s = d.readline()  # Bcz cursor position has come down
# print(s)
# d.seek(0)
# s = d.readline()
# print(s)
f = open("D:\\ElitePFH.txt", "rb")
print("Original Content", f.read())
f.seek(-1, 2)
print(f.read())

d.close()
f.close()
