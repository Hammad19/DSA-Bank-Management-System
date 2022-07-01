from tkinter import *
from tkinter import messagebox

# from LOGIN_FORM import *

NameDetail = None
LnameDetail = None
PasswordDetail = None
PhoneDetail = None
CountryDetail = None
BalanceDetail = None


class Stack:
    cursor = 0
    stack = []

    def push(self, x):
        self.stack[self.cursor] = x
        self.cursor = self.cursor + 1

    def pop(self):
        self.cursor = self.cursor - 1

    def isEmpty(self):
        if self.cursor == -1:
            return True
        else:
            return False

    def top(self):
        return self.stack[self.cursor]


class AccntDetailsWin:

    def __init__(self):

        # Window Properties
        global BalanceDetail, CountryDetail, PhoneDetail, PasswordDetail, LnameDetail, NameDetail, Username, Password
        accntdetails_win = Tk()
        accntdetails_win.geometry("700x500")
        accntdetails_win.title("Account Details")
        accntdetails_win.configure(background='Black')

        # On Load
        for line in open("Static.txt", "r").readlines():
            readstatic = line.split(",")
            Username = readstatic[0]
            Password = readstatic[1]

        for line in open("RegData.txt", "r").readlines():
            login_info = line.split(",")
            if Username == login_info[0]:
                NameDetail = login_info[0]
                LnameDetail = login_info[1]
                PasswordDetail = login_info[2]
                PhoneDetail = login_info[4]
                CountryDetail = login_info[5]
                BalanceDetail = login_info[6]

        # Widgets Declaration
        space1 = Label(accntdetails_win, bg="Black", text="")
        space2 = Label(accntdetails_win, bg="Black", text="")

        lbl1 = Label(accntdetails_win, text="ABC Bank", bg="Black", fg="DodgerBlue", font=("Helvetica", 32))
        lbl2 = Label(accntdetails_win, text="Account Details", bg="Black", fg="DodgerBlue",
                     font=("Arial Bold", 15))

        NameDetaillbl = Label(accntdetails_win, text=NameDetail, bg="Black", fg="Blue2", font=("Arial", 15))
        LnameDetaillbl = Label(accntdetails_win, text=LnameDetail, bg="Black", fg="Blue2",
                               font=("Arial", 15))
        PasswordDetaillbl = Label(accntdetails_win, text=PasswordDetail, bg="Black", fg="Blue2",
                                  font=("Arial", 15))
        PhoneDetaillbl = Label(accntdetails_win, text=PhoneDetail, bg="Black", fg="Blue2",
                               font=("Arial", 15))
        CountryDetaillbl = Label(accntdetails_win, text=CountryDetail, bg="Black", fg="Blue2",
                                 font=("Arial", 15))
        BalanceDetaillbl = Label(accntdetails_win, text=BalanceDetail, bg="Black", fg="Blue2",
                                 font=("Arial", 15))

        # Widgets Implementations
        lbl1.pack()
        lbl2.pack()

        space1.pack()
        space2.pack()

        NameDetaillbl.pack()
        LnameDetaillbl.pack()
        PasswordDetaillbl.pack()
        PhoneDetaillbl.pack()
        CountryDetaillbl.pack()
        BalanceDetaillbl.pack()

        # Loop Of Form
        accntdetails_win.mainloop()
