from tkinter import *
from tkinter.messagebox import showinfo

#import tkinter

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
def reply():
    showinfo(message=Lb1.selection_get())

#window = Tk()
button = Button(top, text='Press', command=reply)
button.pack()


Lb1.pack()
top.mainloop()