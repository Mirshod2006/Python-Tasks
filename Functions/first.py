def mergeLists(list1,list2,list3):
    ls=[]
    if len(list1)==len(list2) and len(list2)==len(list3):
        for i in range(len(list1)):
            newDict = dict()
            insideDict = dict()
            insideDict[list2[i]]=list3[i]
            newDict[list1[i]]=insideDict
            ls.append(newDict)
    print(ls)
ls1= ['S001','S002','S003','S004']
ls2= ['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards']
ls3 = [85,98,89,92]
mergeLists(ls1,ls2,ls3)