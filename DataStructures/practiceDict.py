ls=[1,2,3,4,5]
t = 1,2,3,4,5
s={1,2,3,4,5}
# for i in ls:
#     print(i,end=" ")
# print("\n")
# for i in t:
#     print(i,end=" ")
# print("\n")
# for i in s:
#     print(i,end=" ")

# Set that can be controlled is Dictionary!

d1=dict()
d3 = dict()
print(d1,type(d1))
d2 = {
    1:'hello',
    False:True,
    3.14:'pi',
    'bye':'hello',
    False:0
}
# print(d2.keys())
# print(d2.values())
# print(d2.items())
d1.update(d2)
d3=d2.copy()
d2.pop(3.14)
d2.popitem()
d3.popitem()
d1.clear()
# print(d2.get(False))
# print(d2)
# print(d1)
# print(d3)
l1 = [1,2,3,4,5]
l2 = ['Alex','Andre','Peter','Tom','Tony']
dict2 = dict()
ls=[]
if len(l1)==len(l2):
    for i in range(len(l1)):
        dict2[l1[i]]= l2[i]
print(dict2)
