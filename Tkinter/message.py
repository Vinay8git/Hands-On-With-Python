# --------------------------------------------------------------
# 		MessageBox

# from tkinter import *
# from tkinter.messagebox import showinfo

# from tkinter import *
# from tkinter.messagebox import showinfo
# # from tkinter.ti import ButtonBox
# # import tkinter.messagebox.ABORT
# from tkinter.messagebox import *
# import tkinter

# def reply():
#     print(showinfo(title='popup', message='Button pressed!'))
#     print(tkinter.messagebox.askokcancel("title", "message"))
#     print(tkinter.messagebox.askyesno("title", "message"))
#     print(tkinter.messagebox.askyesnocancel("title", "message"))

# window = Tk()
# button = Button(window, text='press', command=reply)
# button.pack()
# window.mainloop()
# ----------------------------------------------------

# 		radio button

# from tkinter import *

# def sel():
#    selection = "You selected the option " + str(var.get())
#    label.config(text = selection)

# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
#                   command=sel)
# R1.pack( anchor = W )

# R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
#                   command=sel)
# R2.pack( anchor = W )

# R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
#                   command=sel)
# R3.pack( anchor = W)

# label = Label(root)
# label.pack()
# root.mainloop()

# ------------------------------------------------------------------------
# 			Listbox

# from tkinter import *
# from tkinter.messagebox import showinfo

# #import tkinter

# top = Tk()

# Lb1 = Listbox(top)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
# def reply():
#     showinfo(message=Lb1.selection_get())

# #window = Tk()
# button = Button(top, text='press', command=reply)
# button.pack()


# Lb1.pack()
# top.mainloop()