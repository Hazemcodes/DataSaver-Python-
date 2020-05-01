from tkinter import *
import pymysql
import Window2
from tkinter import ttk


try:
    def goback():
        win.destroy()
        Window2.secondWindow()

    def search():
        try:
            db = pymysql.connect(user="User", password="HostPassword!", host="HostURL", database="DatabaseName")
            cursor = db.cursor()
            find = idd.get()
            find = "'"+find+"'"
            sql = 'select * from students where first_name=' + find
            cursor.execute(sql)
            data = cursor.fetchall()
            print(idd.get())
            # ***** Scrollbar *****
            s = Scrollbar(win)
            s.pack(side=RIGHT, fill=Y)

            # ***** Table *****
            tv = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings", height=5, yscrollcommand=s.set)
            tv.column("1", minwidth=30, width=30)
            tv.column("2", minwidth=100, width=100)
            tv.column("3", minwidth=100, width=100)
            tv.column("4", minwidth=200, width=200)
            tv.column("5", minwidth=50, width=50)

            tv.heading(1, text="ID")
            tv.heading(2, text="first_name")
            tv.heading(3, text="second_name")
            tv.heading(4, text="email")
            tv.heading(5, text="gender")

            for i in data:
                tv.insert('', 'end', values=i)
            entry.delete(0, END)
            tv.pack(side=LEFT)
            s.config(command=tv.yview)

        except Exception as ee:
                print("Error " , ee)

    def searchwindow():

        global idd , entry , win
        win = Tk()
        idd = StringVar()

        # ***** Label *****
        Label(win, text="Please Insert The ID", font=30, width=40, bg="#e066ff", fg="blue").place(x=10, y=10)

        # ***** Entry *****
        entry = Entry(win,textvariable=idd,font=20,width=10, bg="white",fg="blue")
        entry.place(x=5,y=60)
        entry.focus()

        # ***** Button *****
        Button(win,text="Search",font=20, background='#ff9900', foreground="black",activebackground="brown", width=8,command=search).place(x=380, y=300)
        Button(win,text="Go Back",font=20,bg="brown", activeforeground="darkblue", activebackground="red", foreground="black", width=8,command=goback).place(x=280, y=300)

        win.title("DataBaseSaver")
        win.geometry("500x390+500+150")
        win.resizable(False,False)
        win['bg']="#e066ff"
        win.mainloop()

except Exception as e :
    print("Error " , e)