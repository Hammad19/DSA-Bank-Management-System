from tkinter import *
from tkinter import messagebox


class HistWin:

    def __init__(self):

        global Username

        for line in open("Static.txt", "r").readlines():
            readstatic = line.split(",")
            Username = readstatic[0]
            Password = readstatic[1]

        def selectionsort():
            print("Selection Sort:")

            lst = []
            for linee in open('Transactions.txt'):
                lst.append(linee.strip())

            n = len(lst)
            for i in range(n):
                min_idx = i
                for j in range(i + 1, len(lst)):
                    line1 = lst[min_idx].split(",")
                    line2 = lst[j].split(",")

                    if int(line1[0]) > int(line2[0]):
                        min_idx = j

                lst[i], lst[min_idx] = lst[min_idx], lst[i]

            for x in range(n):
                xyz = lst[x].split(",")
                if xyz[1] == Username:
                    print(lst[x])

        def quicksort():
            print("Quick Sort:")

            lst = []
            for linea in open('Transactions.txt'):
                lst.append(linea.strip())

            def partition(arr, low, high):
                i = (low - 1)
                pivot = arr[high]

                for j in range(low, high):

                    if arr[j] <= pivot:
                        i = i + 1
                        arr[i], arr[j] = arr[j], arr[i]

                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                return i + 1

            def quick_Sort(arr, low, high):
                if low < high:
                    pi = partition(arr, low, high)

                    quick_Sort(arr, low, pi - 1)
                    quick_Sort(arr, pi + 1, high)
                return arr

            print(quick_Sort(lst, 0, len(lst) - 1))

        # Window Properties
        hist_win = Tk()
        hist_win.geometry("700x500")
        hist_win.title("History")
        hist_win.configure(background='Black')

        # Widgets Declaration
        space1 = Label(hist_win, bg="Black", text="")
        space2 = Label(hist_win, bg="Black", text="")
        space3 = Label(hist_win, bg="Black", text="")
        space4 = Label(hist_win, bg="Black", text="")
        space5 = Label(hist_win, bg="Black", text="")

        lbl1 = Label(hist_win, text="ABC Bank", bg="Black", fg="DodgerBlue", font=("Helvetica", 32))
        lbl2 = Label(hist_win, text="History", bg="Black", fg="DodgerBlue",
                     font=("Arial Bold", 15))

        selectionsrtbtn = Button(hist_win, text="Show Transactions By Amount(Ascending)", width=35, height=2,
                                 bg="Black", fg="Blue2",
                                 command=selectionsort)

        quicksrtbtn = Button(hist_win, text="Show Transactions By Amount(Descending)", width=35, height=2, bg="Black",
                             fg="Blue2",
                             command=quicksort)

        # Widgets Implementations
        lbl1.pack()
        lbl2.pack()

        space1.pack()
        space2.pack()

        selectionsrtbtn.pack()
        quicksrtbtn.pack()

        # Loop Of Form
        hist_win.mainloop()
