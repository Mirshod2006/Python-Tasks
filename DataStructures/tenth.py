def showScatter(num):
    numStr = str(num)
    numList=[]
    for i in range(len(numStr)):
        numList.append(int(numStr[i])*(10**(len(numStr)-1-i)))
    print(*numList,sep="+")
num = int(input("Enter number:"))
showScatter(num)