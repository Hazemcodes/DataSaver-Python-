from tkinter import *
from tkinter import messagebox
import Window2


#  ***** functions *****
def SigninButton():
    Email.set(Email.get().strip())
    if Email.get()=="admin" and Password.get()=="admin" :
        wind1.destroy()
        Window2.secondWindow()
    else :
        Label(wind1,text="wrong",fg="red",bg='#49A').place(x=290,y=350)

def cancelButton():
    messagebox.showwarning("Alert", "canceled")
    wind1.destroy()

def firstWindow():
    global wind1
    wind1 = Tk()
    wind1.title("Login_in")
    wind1.geometry("420x390+500+150")

    # ***** Variables *****
    global Email, Password
    Email = StringVar()
    Password = StringVar()

    #  ***** Images *****
    im1=PhotoImage(file='')

    #  ***** Labels *****
    Label(wind1,text="Sign-In ",font=15, fg="black",bg="#49A").place(x=10,y=10)
    Label(wind1,text="Password",font=15, fg="black",bg="#49A").place(x=10,y=60)


    # ***** Entry *****
    name = Entry(wind1,font= 20,textvariable=Email)
    name.place(x=5,y=35,height=22,width=180)
    name.focus()
    Entry(wind1,textvariable=Password,font= 20,justify=CENTER,show='*').place(x=5,y=85,height=22,width=180)

    #  ***** Buttons *****
    Signin = Button(wind1,text="Sign in",bg="CornflowerBlue",width=8,fg="black",bd=0.5,font=0.5,activeforeground="black",activebackground="blue",command=SigninButton)
    Signin.place(x=230,y=320)

    cancel = Button(wind1,text="cancel",bg="brown",width=8,fg="black",bd=0.5,font=0.5,activeforeground="darkblue",activebackground="red",command=cancelButton)
    cancel.place(x=330,y=320)



    # ***** Main *****
    wind1['bg'] = '#49A'
    wind1.mainloop()


if __name__ == "__main__":
    firstWindow()