def sumTwo(n):
    listOfNum=[]
    sum=0
    num=0
    for i in range(n):
        num = num*10+2
        listOfNum.append(num)
        sum +=num
    print(*listOfNum,sep="+",end="=")
    print(sum)
num = int(input("Enter number:"))
sumTwo(num)