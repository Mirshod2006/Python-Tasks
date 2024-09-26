t1=tuple()
t2=()
t3=(1,2,3,True,False,"Salom","Xayr")
#t3[0]=12321
print(t3.count(True))
print(t3.count("Xayr"))
ls=[("salom",15),("hayr",1),("bolalar",5)]
for i in ls:
    print(*i)
son=int(input("son="))
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i][1]>ls[j][1]:
            ls[i],ls[j]=ls[j],ls[i]
print("======================================")
for i in ls:
    print(*i)
for i in range(len(ls)):
    tp = list(ls[i])
    tp[1] = son
    ls[i] = tuple(tp)
print("######################################")
for i in ls:
    print(*i)
ls.sort()
print("======================================")
for i in ls:
    print(*i)