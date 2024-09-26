import eleventh as some
some.checkZero("0001231")
ls=range(1,11)
oddLs=[]
evenLs=[]
add = lambda x: oddLs.append(x) if x%2!=0 else evenLs.append(x)
for i in ls:
    add(i)
print("Juft:",evenLs)
print("Toq:",oddLs)