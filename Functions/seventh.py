def showEvenFirst(ls):
    strLs1= [str(j) for j in ls]
    strLs2=[]
    for i in strLs1:
        if int(i[0])%2==0:
            strLs2.append(i)
    print(*strLs2,sep=" ")
numLs=[123,456,789,852,12,42,61,369]
showEvenFirst(numLs)