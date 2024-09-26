def showSummation(num):
    sum=0
    str=""
    for i in range(1,num+1):
        sum+=i
        str +=f"{i}"
    print(*str,sep="+",end="=")
    print(sum)
num = int(input("Enter number:"))
showSummation(num)
