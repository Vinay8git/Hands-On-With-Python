from tkinter import *
master=Tk()
master.title("Easy shop")
Label(master,text="Name").grid(row=0)
Label(master,text="Id").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
def insertrecord():
    # con=cx_Oracle.connect("feby/fr@XE")
    # cur=con.cursor()
    name1=e1.get()
    id1=e2.get()
    # cur.execute("insert into emp2(name,id)values('"+ name1 + "'," +id1+ ")")
#name=input("Enter name")


    # con.commit()
    # con.close()
Button(master,text='Add',command=insertrecord).grid(row=4,column=4,sticky=W)
mainloop()