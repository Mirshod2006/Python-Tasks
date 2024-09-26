def dividePrime(num):
    listNum =[]
    k=2
    while num != 1:
        if num%k==0:
            listNum.append(k)
            num = num//k
        else:
            k=k+1
    print(listNum)
num=int(input("Enter number:"))
dividePrime(num)