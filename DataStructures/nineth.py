def showThousands():
    for i in range(1000,9899):
        temp = str(i)
        tempSet = set(temp)
        if len(tempSet) == 4:
            print(i)
showThousands()