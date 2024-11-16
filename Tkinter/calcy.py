#Calculator Code (Solution of Section C Question of AKTU Paper 2023) 
import tkinter as tk 
def b1Click(event): 
 s=t1.get() 
 s=s+"1" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b2Click(event): 
 s=t1.get() 
 s=s+"2" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b3Click(event): 
 s=t1.get() 
 s=s+"3" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b4Click(event): 
 s=t1.get() 
 s=s+"4" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b5Click(event): 
 s=t1.get() 
 s=s+"5" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b6Click(event): 
 s=t1.get() 
 s=s+"6" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b7Click(event): 
 s=t1.get() 
 s=s+"7" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b8Click(event): 
 s=t1.get() 
 s=s+"8" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b9Click(event): 
 s=t1.get() 
 s=s+"9" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def b0Click(event): 
 s=t1.get() 
 s=s+"0" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def baddClick(event): 
 s=t1.get() 
 s=s+"+" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def bsubClick(event): 
 s=t1.get() 
 s=s+"-" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def bmulClick(event): 
 s=t1.get() 
 s=s+"*" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def bdivClick(event): 
 s=t1.get() 
 s=s+"/" 
 t1.delete(0,'end') 
 t1.insert(0,s) 
def bequClick(event): 
 s=t1.get() 
 a=eval(s) 
 t1.delete(0,'end') 
 t1.insert(0,a) 
def bacClick(event): 
 t1.delete(0,'end') 
def bcClick(event): 
 s=t1.get() 
 s1=s[0:-1] 
 t1.delete(0,'end') 
 t1.insert(0,s1) 
root=tk.Tk() 
root.geometry("400x400") 
t1=tk.Entry(root,width=60) 
t1.grid(row=0,column=0,columnspan=5) 
b1=tk.Button(root,text="1",width=8,height=3,bg='orange') 
b1.grid(row=1,column=0) 
b2=tk.Button(root,text="2",width=8,height=3) 
b2.grid(row=1,column=1) 
b3=tk.Button(root,text="3",width=8,height=3) 
b3.grid(row=1,column=2) 
bc=tk.Button(root,text="C",width=8,height=3) 
bc.grid(row=1,column=3) 
bac=tk.Button(root,text="AC",width=8,height=3) 
bac.grid(row=1,column=4) 
b4=tk.Button(root,text="4",width=8,height=3) 
b4.grid(row=2,column=0) 
b5=tk.Button(root,text="5",width=8,height=3) 
b5.grid(row=2,column=1) 
b6=tk.Button(root,text="6",width=8,height=3) 
b6.grid(row=2,column=2) 
badd=tk.Button(root,text="+",width=8,height=3) 
badd.grid(row=2,column=3) 
bsub=tk.Button(root,text="-",width=8,height=3) 
bsub.grid(row=2,column=4) 
b7=tk.Button(root,text="7",width=8,height=3) 
b7.grid(row=3,column=0) 
b8=tk.Button(root,text="8",width=8,height=3) 
b8.grid(row=3,column=1) 
b9=tk.Button(root,text="9",width=8,height=3) 
b9.grid(row=3,column=2) 
bmul=tk.Button(root,text="*",width=8,height=3) 
bmul.grid(row=3,column=3) 
bdiv=tk.Button(root,text="/",width=8,height=3) 
bdiv.grid(row=3,column=4) 
bpm=tk.Button(root,text="+/-",width=8,height=3) 
bpm.grid(row=4,column=0) 
b0=tk.Button(root,text="0",width=8,height=3) 
b0.grid(row=4,column=1) 
bdec=tk.Button(root,text=".",width=8,height=3) 
bdec.grid(row=4,column=2) 
bequ=tk.Button(root,text="=",width=18,height=3,fg='blue') 
bequ.grid(row=4,column=3,columnspan=2) 
b1.bind("<Button-1>",b1Click) 
b2.bind("<Button-1>",b2Click) 
b3.bind("<Button-1>",b3Click) 
b4.bind("<Button-1>",b4Click) 
b5.bind("<Button-1>",b5Click) 
b6.bind("<Button-1>",b6Click) 
b7.bind("<Button-1>",b7Click) 
b8.bind("<Button-1>",b8Click) 
b9.bind("<Button-1>",b9Click) 
b0.bind("<Button-1>",b0Click) 
badd.bind("<Button-1>",baddClick) 
bsub.bind("<Button-1>",bsubClick) 
bmul.bind("<Button-1>",bmulClick) 
bdiv.bind("<Button-1>",bdivClick) 
bequ.bind("<Button-1>",bequClick) 
bac.bind("<Button-1>",bacClick) 
bc.bind("<Button-1>",bcClick) 
root.mainloop()