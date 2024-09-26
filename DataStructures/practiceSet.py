s1 = set()
# there is difference between union and update
# never forget union works with print(),but
#  will not update the set really!
s1 = set()
ls1 = [1,2,3,41,2,4,1,89,0,5,1,3,5,8]
ls1 = set(ls1)
print(*ls1)
ls = [{1,2,3},{4,5,7},{6,8,9}]
nl = list()
for i,j,k in ls:
    nl.append(i)
    nl.append(j)
    nl.append(k)
print(*nl)
# Inside, the list elements we can use nearly any kind of data types 
# even tuples , sets and lists can be used!