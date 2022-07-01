from tkinter import *
from ACCOUNTDETAILS_FORM import AccntDetailsWin
from HISTORY_FORM import HistWin
from TOPUP_FORM import TopUpWin
from TRANSFER_FORM import TransferWin


class MainWin:

    def __init__(self):
        def Histopen():
            hww = HistWin()

        def Transferopen():
            tww = TransferWin()

        def Topupopen():
            tpww = TopUpWin()

        def AccntDetailsopen():
            aww = AccntDetailsWin()

        # Window Properties
        main_win = Tk()
        main_win.geometry("700x500")
        main_win.title("Home")
        main_win.configure(background='Black')

        # Widgets Declaration
        space1 = Label(main_win, bg="Black", text="")
        space2 = Label(main_win, bg="Black", text="")
        space3 = Label(main_win, bg="Black", text="")
        space4 = Label(main_win, bg="Black", text="")
        space5 = Label(main_win, bg="Black", text="")
        space6 = Label(main_win, bg="Black", text="")

        lbl1 = Label(main_win, text="ABC Bank", bg="Black", fg="DodgerBlue", font=("Helvetica", 32))
        lbl2 = Label(main_win, text="Home Page", bg="Black", fg="DodgerBlue",
                     font=("Arial Bold", 15))

        HistBtn = Button(main_win, text="History", width=15, height=2, bg="Black", fg="Blue2", command=Histopen)
        TransBtn = Button(main_win, text="Transfer Funds", width=15, height=2, bg="Black", fg="Blue2",
                          command=Transferopen)
        TopupBtn = Button(main_win, text="Mobile Balance", width=15, height=2, bg="Black", fg="Blue2",
                          command=Topupopen)
        AcntDetailBtn = Button(main_win, text="Acccount Details", width=15, height=2, bg="Black", fg="Blue2",
                               command=AccntDetailsopen)

        # Widgets Implementations

        lbl1.pack()
        lbl2.pack()

        space1.pack()
        space2.pack()

        HistBtn.pack()
        space3.pack()
        TransBtn.pack()
        space5.pack()
        TopupBtn.pack()
        space6.pack()
        AcntDetailBtn.pack()

        # Loop Of Form

        main_win.mainloop()
