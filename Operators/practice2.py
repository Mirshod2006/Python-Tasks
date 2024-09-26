# or and not
num =int(input("Enter num:"))
k=2
j=0
while 1:
    if num%k==0:
        j=j+1
    if k==num/2:
        break
    k=k+1
if j==0:
    print("It is Prime number!")
else:
    print("It is not a prime number!")
# bittali bo'luv qoldiqli bo'lish 
# ikki tali bo'luv butunli bo'lish
# EXAMPLE:
son = int(input("Enter number:"))
while son!=0:
    print(son%10,end=' ')
    son=son//10
'''#
siulhfiuerhfpiewurbgiupehbg
k;ennergniewbgibweibre
sknfebberubgwybyvuebyrbv
vjherbveurybybveiybiebri
gfxhdyjyt
dfhjtyjrukt
jtykjkyukyjtyhdrjduye'''
# string.lower()
# string.upper()
# string type cannot be changed by indexing,it can be only with 
# replace function()
new = ""
for i in str:
    if i=='a':
        new=new+'o'
    elif i=='A':
        new=new+'O'
    elif i=='o':
        new=new+'a'
    elif i=='O':
        new=new+'A'
    else:
        new=new+i
str=str.replace(str,new)
print(str)