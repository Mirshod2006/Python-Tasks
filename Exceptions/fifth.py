def findSum():
    ls=[]
    while(True):
        n=input()
        if n=='c':
            break
        if n.isdigit():
            ls.append(int(n))
    sum=0
    for i in ls:
        sum+=i
    print(sum)
findSum()