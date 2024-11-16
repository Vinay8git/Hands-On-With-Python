import os
# print(os.getcwd())
# os.chdir("D:\\WEB")
# print(os.getcwd())

# fp=open("pfh.txt","w")
# fp.write("Hello, world!")
#
# print(fp.closed)
# print(fp.name)
# print(fp.mode)

# os.mkdir("C:\\Users\\dell\\Desktop\\Python\\New")
# os.rmdir("C:\\Users\\dell\\Desktop\\Python\\New")
# os.rename('Adhura S01 Hindi 720p WEBDL ESub [BollyFlix]','Adhura S01')

# try:
#     fp = ("pfhh.txt", "x")
#     print(fp.read())
# except Exception as e:
#     print(e)
# finally:
#     print("Want To Rename Or Make A New File")
#     print("R / N : ")
#     ch = input("Enter Choice: ")
#     if ch == 'R':
#         os.rename('pfh.txt', 'pfhh.txt')
#     if ch == 'N':
#         fp = open("pfh.txt", "w")
#         fp.write("Hello, world!")

# f = open("C:\\Users\\dell\\Desktop\\Python\\AT1.py", "r")
# s = f.readline()
# while s:
#     if s.startswith("#"):
#         print(s)
#     s = f.readline()

print(os.getcwd())
# os.mkdir("C:\\Users\\dell\\Desktop\\Python\\Assignment")
os.chdir("C:\\Users\\dell\\Desktop\\Python\\Assignment")
print(os.getcwd())
f=open("Asg-27Dec.py","w")
f.write("import os")
f.close()