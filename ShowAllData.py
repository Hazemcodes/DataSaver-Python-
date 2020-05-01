from tkinter import *
from tkinter import ttk
import pymysql
import Window2

def back():
    win.destroy()
    Window2.secondWindow()

def show():
    global win
    win = Tk()
    frm = Frame(win)
    frm.pack(padx=20, pady=20)

    db = pymysql.connect(user="User", password="HostPassword!", host="HostURL", database="DatabaseName")
    cursor = db.cursor()
    sql = 'select * from students'
    cursor.execute(sql)
    rows = cursor.fetchall()

    s = Scrollbar(frm)
    s.pack(side=RIGHT,fill=Y)

    tv = ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings",height=20,yscrollcommand=s.set)
    tv.column("1",minwidth = 30,width=30)
    tv.column("2",minwidth = 100, width=100)
    tv.column("3",minwidth = 100, width=100)
    tv.column("4",minwidth = 200, width=200)
    tv.column("5",minwidth = 50, width=50)

    tv.heading(1,text="ID")
    tv.heading(2,text="first_name")
    tv.heading(3,text="second_name")
    tv.heading(4,text="email")
    tv.heading(5,text="gender")

    for i in rows :
        tv.insert('','end',values=i)

    Button(win,text="Go Back",bg="brown", activeforeground="darkblue", activebackground="red", foreground="black",width=8,command=back).place(x=520,y=456)

    tv.pack(side=LEFT,fill=BOTH)
    s.config(command=tv.yview)
    win.title("")
    win.geometry("600x500+500+150")
    win.resizable(False,False)
    win['bg']="#00cc00"
    win.mainloop()

if __name__ == '__main__':
    show()