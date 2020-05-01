import pymysql
from tkinter import *
import Window1
import Search
import ShowAllData

try:

    def Signout():
        wind2.destroy()
        Window1.firstWindow()

    def show():
        wind2.destroy()
        ShowAllData.show()

    def search():
        wind2.destroy()
        Search.searchwindow()

    def secondWindow():
        global wind2
        wind2 = Tk()


        # ***** Variables *****
        text = StringVar()  # work signin or no #LAbel
        global FirstName, SecondName, Email, vr, FirstNameEn, SecondNameEn, EmailEn
        FirstName = StringVar()
        SecondName = StringVar()
        Email = StringVar()
        cc = IntVar()
        vr = IntVar()  # vr = variable radiobutton

        # ***** Label *****
        Label(wind2,text="Welcome", font=25, fg="black",bg="#4da6ff").place(x=250, y=20)
        Label(wind2,text="Hazem", font=25, fg="black",bg="#4da6ff").place(x=320,y=20)
        Label(wind2,text="First Name", font=15, fg="black",bg="#4da6ff").place(x=10,y=10)
        Label(wind2,text="Second Name", font=15, fg="black",bg="#4da6ff").place(x=10,y=60)
        Label(wind2,text="Email", font=15, fg="black",bg="#4da6ff").place(x=10,y=110)


        # ***** Entry *****
        FirstNameEn = Entry(wind2,textvariable=FirstName)
        FirstNameEn.place(x=5,y=35,height=22,width=180)
        SecondNameEn = Entry(wind2,textvariable=SecondName)
        SecondNameEn.place(x=5,y=85,height=22,width=180)
        EmailEn = Entry(wind2,textvariable=Email)
        EmailEn.place(x=5,y=135,height=22,width=180)


        # ***** RadioButton *****
        Radiobutton(wind2, text="male", variable=vr, value=1,bg="#4da6ff").place(x=30,y=180)
        Radiobutton(wind2, text="female", variable=vr, value=2,bg="#4da6ff").place(x=90,y=180)

        # ***** Button *****
        b1 = Button(wind2, text="Add", bg="CornflowerBlue", width=8, fg="black", bd=0.5, font=0.5,activeforeground="black", activebackground="blue",command=add)
        b1.place(x=230, y=320)
        b2 = Button(wind2, text="Sign-out", bg="brown", width=8, fg="black", bd=0.5, font=0.5,activeforeground="darkblue", activebackground="red",command=Signout)
        b2.place(x=330, y=320)
        b3 = Button(wind2, text="Show All", bg="DarkOrange", width=8, fg="black", bd=0.5, font=0.5,activeforeground="black", activebackground="DarkGoldenRod", command=show)
        b3.place(x=130, y=320)
        b3 = Button(wind2, text="Search", bg="#e066ff", width=8, fg="black", bd=0.5, font=0.5,activeforeground="black", activebackground="#993399", command=search)
        b3.place(x=30, y=320)

        # ***** Main *****
        wind2.title("DataBaseSaver")
        wind2.geometry("420x390+500+150")
        wind2['bg']="#4da6ff"
        wind2.mainloop()

    def add():
        first_name = FirstNameEn.get()
        second_name = SecondNameEn.get()
        email = EmailEn.get()
        gender = ""
        if vr.get() == 1:
            gender = "male"
        elif vr.get() == 2:
            gender = "female"
        try:
            db = pymysql.connect(user="sql2331957", password="aG1!fW9!", host="sql2.freesqldatabase.com",database="sql2331957")
            cursor = db.cursor()
            cursor.execute(
                 'INSERT INTO students(first_name,second_name,email,gender) values(%s,%s,%s,%s)',
                 (first_name, second_name, email, gender))

        except Exception as e:
             print("Error ", e)
        finally:
             db.commit()
             cursor.close()
             db.close()

        FirstNameEn.delete(0, END)
        SecondNameEn.delete(0, 'end')
        EmailEn.delete(0, END)
        vr.set(0)

    def datbase():
        try:
            db = pymysql.connect(user="sql2331957", password="aG1!fW9!", host="sql2.freesqldatabase.com",database="sql2331957")
            cursor = db.cursor()
            cursor.execute(
                'CREATE TABLE if not exists students(id INT(11) NOT NULL AUTO_INCREMENT ,first_name varchar(255) NOT NULL ,second_name varchar(255) NOT NULL,email varchar(255),gender varchar(255) NOT NULL,CONSTRAINT contacts_pk PRIMARY KEY (id))')

        except Exception as e:
            print("no", e)
        finally:
            db.commit()
            cursor.close()
            db.close()
except Exception as e:
        print("Error ", e)