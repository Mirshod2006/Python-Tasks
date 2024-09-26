def showIndexes(ls,num):
    space = False
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]+ls[j]==num:
                print(f"({i},{j})")
                space=True
        if(space):
            print(" ")
a = int(input("Input number:"))
ls = [1,2,33,5,6,7,7]
showIndexes(ls,a)