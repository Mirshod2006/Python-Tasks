import random as r
import math as m
def showPrimes():
    ls = [r.randint(1,1000000) for _ in range(1000)]
    prime_list=[]
    start_point = ls[r.randint(0,999)]

    for i in range(max(2,start_point),1000000):
        prime = True
        if i==2:
            prime_list.append(i)
        if i%2==0:
            continue
        for j in range(2,int(m.sqrt(i))+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            prime_list.append(i)
    print(*prime_list,sep=" ")
showPrimes()