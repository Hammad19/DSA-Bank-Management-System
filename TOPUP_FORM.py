from tkinter import *
from tkinter import messagebox
import os

# Variable Declaration
Account = None
Amount = None


class TopUpWin:

    def __init__(self):

        def Transaction():

            global BalanceDetail, Username

            for line in open("Static.txt", "r").readlines():
                readstatic = line.split(",")
                Username = readstatic[0]
                Password = readstatic[1]

            for line in open("RegData.txt", "r").readlines():
                login_info = line.split(",")
                if Username == login_info[0]:
                    NameDetail = login_info[0]
                    BalanceDetail = login_info[6]

            Account = "Phone"
            Amount = Amntaccntent.get()

            Typeoftransaction = "Top-Up"

            if int(BalanceDetail) > int(Amount):

                BalanceDetail = int(BalanceDetail) - int(Amount)
                messagebox.showinfo("Remaining Balance", BalanceDetail)

                # Write Values in Temp
                for line in open("RegData.txt", "r").readlines():
                    login_info = line.split(",")
                    if Username == login_info[0]:
                        NameDetail = login_info[0]
                        LnameDetail = login_info[1]
                        PasswordDetail = login_info[2]
                        RepasswordDetail = login_info[3]
                        PhoneDetail = login_info[4]
                        CountryDetail = login_info[5]

                        sw = open("Temp.txt", "a")
                        sw.write(
                            NameDetail + "," + LnameDetail + "," + PasswordDetail + "," + RepasswordDetail + "," + PhoneDetail + "," + CountryDetail + "," + str(
                                BalanceDetail) + "\n")
                        sw.close()

                        sww = open("Transactions.txt", "a")
                        sww.write(Amount + "," + NameDetail + "," + Account + "," + Typeoftransaction + "," +str(BalanceDetail) + "\n")
                        sww.close()
                    else:
                        sw = open("Temp.txt", "a")
                        sw.write(line)
                        sw.close()
                os.remove("RegData.txt")

                with open("Temp.txt") as f:
                    with open("RegData.txt", "w") as f1:
                        for line in f:
                            f1.write(line)
                os.remove("Temp.txt")

            else:
                messagebox.showinfo("Error", "Insufficient Funds")

        # Window Properties
        Topup_win = Tk()
        Topup_win.geometry("700x500")
        Topup_win.title("Top Up")
        Topup_win.configure(background='Black')

        # Widgets Declaration
        space1 = Label(Topup_win, bg="Black", text="")
        space2 = Label(Topup_win, bg="Black", text="")
        space3 = Label(Topup_win, bg="Black", text="")
        space4 = Label(Topup_win, bg="Black", text="")
        space5 = Label(Topup_win, bg="Black", text="")
        space6 = Label(Topup_win, bg="Black", text="")

        lbl1 = Label(Topup_win, text="ABC Bank", bg="Black", fg="DodgerBlue", font=("Helvetica", 32))
        lbl2 = Label(Topup_win, text="Mobile Top Up", bg="Black", fg="DodgerBlue",
                     font=("Arial Bold", 15))

        Amntaccntlbl = Label(Topup_win, text="Amount To Transfer:", bg="Black", fg="Blue2", font=("Arial", 15))
        Amntaccntent = Entry(Topup_win, textvariable=Amount)

        TransferBtn = Button(Topup_win, text="Transfer", width=12, height=2, bg="Black", fg="Blue2",
                             command=Transaction)

        # Widgets Implementations
        lbl1.pack()
        lbl2.pack()

        space1.pack()
        space2.pack()

        space3.pack()
        space4.pack()

        Amntaccntlbl.pack()
        Amntaccntent.pack()

        space5.pack()
        space6.pack()

        TransferBtn.pack()

        # Loop Of Form
        Topup_win.mainloop()
