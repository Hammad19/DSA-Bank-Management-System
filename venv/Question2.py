a = [37, 88, 45, 12, 70, 1, 90, 22, 11, 90]


def xyz(myArr):
    n = len(myArr)
    for x in range(n):
        print(myArr)
        for y in range(0, n - x - 1):
            if myArr[y] > myArr[y + 1]:
                myArr[y], myArr[y + 1] = myArr[y + 1], myArr[y]





xyz(a)