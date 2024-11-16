from tkinter import *

root = Tk()
frame = Frame(root,bg="red")
frame.pack(ipady=40,ipadx=40)

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM,pady=200 )

centerframe=Frame(root)
centerframe.pack(side=LEFT,padx=150 )
b1=Button(centerframe,text="center frame")
b1.pack(side=LEFT)
b2=Button(centerframe,text="center frame 2" )
b2.pack(side=LEFT)

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT,padx=20)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT,padx=5 )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black button2", fg="black")
blackbutton.pack( side = LEFT)


blackbutton2 = Button(bottomframe, text="Black button", fg="black")
blackbutton2.pack( side = LEFT)

root.mainloop()