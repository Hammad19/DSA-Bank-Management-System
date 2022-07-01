from tkinter import *
from tkinter import messagebox

# Variable Declaration
Fname = None
Lname = None
Password = None
Repassword = None
Phone = None
Age = None
Amount = None


class RegistrationWin:

    def __init__(self):

        def RegToFile():

            # Add values
            Fname = fnameent.get()
            Lname = lnameent.get()
            Password = pwdent.get()
            Repassword = rpwdent.get()
            Phone = phoneent.get()
            Age = ageent.get()
            Amount = amountent.get()

            if Password == Repassword:
                # Text file
                sw = open("RegData.txt", "a")
                sw.write(
                    Fname + "," + Lname + "," + Password + "," + Repassword + "," + Phone + "," + Age + "," + Amount + "\n")
                sw.close()
                messagebox.showinfo("Congratulation", "Registration Sucessfull")
            else:
                messagebox.showinfo("Failure", "Passwords Don't Match")

        # Window Properties
        regwin = Tk()
        regwin.geometry("700x500")
        regwin.title("Registration")
        regwin.configure(background='Black')

        # Widgets Declaration
        space1 = Label(regwin, bg="Black", text="")
        space2 = Label(regwin, bg="Black", text="")
        space3 = Label(regwin, bg="Black", text="")
        space4 = Label(regwin, bg="Black", text="")
        space5 = Label(regwin, bg="Black", text="")

        lbl1 = Label(regwin, text="ABC Bank", bg="Black", fg="DodgerBlue", font=("Helvetica", 32))
        lbl2 = Label(regwin, text="Registration Form", bg="Black", fg="DodgerBlue", font=("Arial Bold", 15))
        fnamelbl = Label(regwin, text="First Name:", bg="Black", fg="DodgerBlue", font=("Arial", 12))
        lnamelbl = Label(regwin, text="Last Name:", bg="Black", fg="DodgerBlue", font=("Arial", 12))
        pwdlbl = Label(regwin, text="Password:", bg="Black", fg="DodgerBlue", font=("Arial", 12))
        rpwdlbl = Label(regwin, text="Re-Enter Password:", bg="Black", fg="DodgerBlue", font=("Arial", 12))
        phonelbl = Label(regwin, text="Phone no:", bg="Black", fg="DodgerBlue", font=("Arial", 12))
        agelbl = Label(regwin, text="Age:", bg="Black", fg="DodgerBlue", font=("Arial", 12))
        amountlbl = Label(regwin, text="Amount:", bg="Black", fg="DodgerBlue", font=("Arial", 12))

        fnameent = Entry(regwin, textvariable=Fname)
        lnameent = Entry(regwin, textvariable=Lname)
        pwdent = Entry(regwin, textvariable=Password)
        rpwdent = Entry(regwin, textvariable=Repassword)
        phoneent = Entry(regwin, textvariable=Phone)
        ageent = Entry(regwin, textvariable=Age)
        amountent = Entry(regwin, textvariable=Amount)

        Regbtn = Button(regwin, text="Register Here", width=10, height=1, bg="Black", fg="Blue2", command=RegToFile)

        # Widgets Implementations
        lbl1.pack()
        lbl2.pack()

        space1.pack()
        space2.pack()

        fnamelbl.pack()
        fnameent.pack()

        lnamelbl.pack()
        lnameent.pack()

        pwdlbl.pack()
        pwdent.pack()

        rpwdlbl.pack()
        rpwdent.pack()

        phonelbl.pack()
        phoneent.pack()

        agelbl.pack()
        ageent.pack()

        amountlbl.pack()
        amountent.pack()

        space3.pack()

        Regbtn.pack()

        # Loop Of Form
        regwin.mainloop()
