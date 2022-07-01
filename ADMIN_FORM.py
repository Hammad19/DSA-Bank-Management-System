from tkinter import *
from tkinter import messagebox


class AdminWin:

    def __init__(self):

        def bblesort():
            print("Bubble Sort:")

            lst = []
            for linee in open('RegData.txt'):
                lst.append(linee.strip())

            n = len(lst)
            for i in range(n):

                for j in range(0, n - i - 1):

                    if lst[j] > lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]

            for x in range(n):
                print(lst[x])

        def insrtsort():
            print("Insertion Sort:")

            lst = []
            for linee in open('RegData.txt'):
                lst.append(linee.strip())

            n = len(lst)

            for i in range(1, len(lst)):
                j = i
                while j > 0 and lst[j] > lst[j - 1]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                    j -= 1

            for x in range(n):
                print(lst[x])

        def mergesrt():

            Userfind = Userent.get()

            lst = []
            for linee in open('RegData.txt'):
                lst.append(linee.strip())

            def mergeSort(arr):

                if len(arr) > 1:
                    mid = len(arr) // 2
                    L = arr[:mid]
                    R = arr[mid:]

                    mergeSort(L)
                    mergeSort(R)

                    i = j = k = 0

                    while i < len(L) and j < len(R):
                        if L[i] < R[j]:
                            arr[k] = L[i]
                            i += 1
                        else:
                            arr[k] = R[j]
                            j += 1
                        k += 1

                    while i < len(L):
                        arr[k] = L[i]
                        i += 1
                        k += 1

                    while j < len(R):
                        arr[k] = R[j]
                        j += 1
                        k += 1
                return arr

            def binarySearch(arr, x):
                values = []
                g = 0
                r = len(arr)
                while g <= r:

                    m = int(g + ((r - g) / 2))
                    values = arr[m].split(",")
                    res = (x == values[0])

                    if res == 0:
                        return m - 1

                    if res > 0:
                        g = m + 1

                    else:
                        r = m - 1
                return -1

            datatosearch = Userfind
            result = binarySearch(mergeSort(lst), datatosearch)
            if result == -1:
                print("Not Found")
            else:
                print(mergeSort(lst)[result - 1])

        # Window Properties
        admin_win = Tk()
        admin_win.geometry("700x500")
        admin_win.title("Admin")
        admin_win.configure(background='Black')

        # Widgets Declaration
        space1 = Label(admin_win, bg="Black", text="")
        space2 = Label(admin_win, bg="Black", text="")
        space3 = Label(admin_win, bg="Black", text="")
        space4 = Label(admin_win, bg="Black", text="")
        space5 = Label(admin_win, bg="Black", text="")

        lbl1 = Label(admin_win, text="ABC Bank", bg="Black", fg="DodgerBlue", font=("Helvetica", 32))
        lbl2 = Label(admin_win, text="Admin Panel", bg="Black", fg="DodgerBlue",
                     font=("Arial Bold", 15))

        bublesrtbtn = Button(admin_win, text="Show Users(Ascending)", width=20, height=2, bg="Black", fg="Blue2",
                             command=bblesort)

        insrtsrtbtn = Button(admin_win, text="Show Users(Descending)", width=20, height=2, bg="Black", fg="Blue2",
                             command=insrtsort)

        findlbl = Label(admin_win, text="User To Search:", bg="Black", fg="Blue2", font=("Arial", 15))

        mergesrtbtn = Button(admin_win, text="Search Users", width=20, height=2, bg="Black", fg="Blue2",
                             command=mergesrt)

        Userent = Entry(admin_win)

        # Widgets Implementations
        lbl1.pack()
        lbl2.pack()

        space1.pack()
        space2.pack()

        bublesrtbtn.pack()
        insrtsrtbtn.pack()

        space3.pack()
        findlbl.pack()
        Userent.pack()
        mergesrtbtn.pack()

        # Loop Of Form
        admin_win.mainloop()
