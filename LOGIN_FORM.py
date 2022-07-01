from tkinter import *
from tkinter import messagebox
from MAIN_FORM import *
from REGISTRATION_FORM import RegistrationWin
from ADMIN_FORM import AdminWin
import os

class LoginWin:
    def __init__(self):
        if os.path.exists("Static.txt"):
            os.remove("Static.txt")
        def LoginVerf():
            global check

            Password = Passwordent.get()
            Username = Usernameent.get()

            # Text file

            sw = open("Static.txt", "a")
            sw.write(Username + "," + Password + "\n")
            sw.close()

            if Username == "admin" and Password == "admin":
                aw = AdminWin()

            else:
                for line in open("RegData.txt", "r").readlines():
                    login_info = line.split(",")
                    if Username == login_info[0] and Password == login_info[2]:
                        check = 1
                        break
                    else:
                        check = 0

                if check == 1:
                    mw = MainWin()

                else:
                    messagebox.showinfo("Error", "Login Unsucessfull")

        def RegBtnFunc():
            rw = RegistrationWin()

        # Window Properties
        loginwin = Tk()
        loginwin.geometry("700x500")
        loginwin.title("Login")
        loginwin.configure(background='Black')

        # Widgets Declaration
        space1 = Label(loginwin, bg="Black", text="")
        space2 = Label(loginwin, bg="Black", text="")
        space3 = Label(loginwin, bg="Black", text="")
        space4 = Label(loginwin, bg="Black", text="")

        lbl1 = Label(loginwin, text="Welcome to HU Bank", bg="Black", fg="DodgerBlue", font=("Helvetica", 32))
        lbl2 = Label(loginwin, text="Please Enter Your Details Below To Continue", bg="Black", fg="DodgerBlue",
                     font=("Arial Bold", 15))

        Usernamelbl = Label(loginwin, text="Username:", bg="Black", fg="Blue2", font=("Arial", 15))
        Usernameent = Entry(loginwin)

        Passwordlbl = Label(loginwin, text="Password:", bg="Black", fg="Blue2", font=("Arial", 15))
        Passwordent = Entry(loginwin, show='*')

        loginbtn = Button(loginwin, text="Login", width=10, height=1, bg="Black", fg="Blue2", command=LoginVerf)

        RegPromptlbl = Label(loginwin, text="Not Already A User?", bg="Black", fg="DodgerBlue", font=("Arial", 10))

        Regbtn = Button(loginwin, text="Register Here", width=10, height=1, bg="Black", fg="Blue2", command=RegBtnFunc)

        # Widgets Implementations
        lbl1.pack()
        lbl2.pack()

        space1.pack()
        space2.pack()

        Usernamelbl.pack()
        Usernameent.pack()
        Usernameent.focus()

        Passwordlbl.pack()
        Passwordent.pack()

        space3.pack()

        loginbtn.pack()

        space4.pack()

        RegPromptlbl.pack()
        Regbtn.pack()

        loginwin.mainloop()


lw = LoginWin()
# Loop Of Form
