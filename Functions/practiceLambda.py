sum = lambda x,y: x+y
print(sum(10,20))
text = input("Enter some text:")
(lambda text: print(text," "))(text)
ls=[1,6,2,5,3,3,5,2,5,3,5,7,2,7,24,5]
l1=list(filter(lambda x:x%2==0,ls))
print(l1)
m1=list(map(lambda z:z%2==0,ls))
print(m1)