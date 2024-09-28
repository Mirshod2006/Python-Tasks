import random as r
def findTillRandomNumber():
    ls=[]
    num_list = []
    for i in range(100):
        ls.append(r.randint(100, 1000))
    for i in range(1,ls[r.randint(1,100)]):
        if i%2==0:
            num_list.append(i)
    print(*num_list,sep=" ")
findTillRandomNumber()