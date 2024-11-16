# from tkinter import *
#
# root = Tk()
# root.maxsize(555, 555)
# root.minsize(555, 555)
# w = Label(root, text="Red Sun", bg="red", fg="white")
# w.pack(fill=X,padx=120,pady=80)
# w = Label(root, text="Green Grass", bg="green", fg="black")
# w.pack(fill=X,padx=120,pady=80)
# w = Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack(fill=X,padx=120,pady=80)
#
# mainloop()
# from tkinter import *
# root = Tk()
# root.maxsize(555, 555)
# root.minsize(555, 555)
# w = Label(root, text="Red Sun", bg="red", fg="white")
# w.pack()
# w = Label(root, text="Green Grass", bg="green", fg="black")
# w.pack(ipadx=10)
# #w.pack(ipady=10)
# w = Label(root, text="Blue Sky", bg="blue", fg="white")
# w.pack()
# mainloop()
# from tkinter import *
#
# root = Tk()
#
# w = Label(root, text="red", bg="red", fg="white")
# w.pack(padx=2, pady=1)
# w = Label(root, text="green", bg="green", fg="black")
# w.pack(padx=2, pady=1)
# w = Label(root, text="blue", bg="blue", fg="white")
# w.pack(padx=2, pady=1)
#
# mainloop()
from tkinter import *

colours = ['red','green','orange','white','yellow','blue']

r = 10
for c in colours:
    Label(text=c, relief=RIDGE,width=10).grid(row=r,column=0,pady=20,padx=50)
    Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1,ipadx=30)
    r = r + 1

mainloop()