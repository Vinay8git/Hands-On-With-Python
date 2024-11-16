from tkinter import *
from tkinter import filedialog
import subprocess, sysconfig
import os


def donothing():
    filewin = Toplevel(root)
    filewin.minsize(555, 555)
    filewin.maxsize(555, 555)

    button = Button(filewin, text="Do nothing button")
    # doc=Document( filedialog.askopenfilename())

    os.startfile(filedialog.askopenfilename())
    # subprocess.Popen( "calc.exe")

    # subprocess.Popen( "notepad")

    button.pack()


'''def donothing():
   form1 = Tk()
   form1.minsize(555, 555)
   form1.maxsize(555, 555)
   button = Button(form1, text="Do nothing button")
   button.pack()'''
root = Tk()
root.minsize(666, 666)
root.maxsize(666, 666)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)  # to avoid dashed line
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Open", command=)

filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()