list1=list()
list2=[]
list3=[123,32.4,'M',"Hello My Brothers",False,False,True,123,'M']
print(list3.count('M'))
print(list3.count(123))
print(list3.count(False))
print(list3)
list3.pop()
print(*list3) # without braces and separators data will be shown
list3.remove('M')
for i in list3:
    print(i)
list1.append("Misha")
list1.insert(3,"Forget!")
#list1.clear()
print(*list1)
list3.reverse()
print(*list3)