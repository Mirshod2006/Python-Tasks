figure = {1,2,3,4,5,6,7,8,9,10}
num = int(input("Enter natural number:"))
if num in figure:   
    for i in figure:
        print(num,"*",i,"=",num*i)