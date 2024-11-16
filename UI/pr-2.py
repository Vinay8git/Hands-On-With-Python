from tkinter import *
from tkinter.messagebox import showinfo

from tkinter import *
from tkinter.messagebox import showinfo
#from tkinter.ti import ButtonBox
#import tkinter.messagebox.ABORT
from tkinter.messagebox import *
import tkinter

def reply():
    #print(showinfo(title='popup', message='Button pressed!'))
    #print(tkinter.messagebox.askokcancel("title", "message"))
    #print(tkinter.messagebox.askyesno("title", "message"))
    print(tkinter.messagebox.askyesnocancel("Warning", "Virus"))

window = Tk()
button = Button(window, text='Press', command=reply)
button.pack()
window.mainloop()