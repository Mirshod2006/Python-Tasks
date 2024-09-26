number = "210"
def checkZero(number):
    count=0
    for i in number:
        if i=='0':
            count=count+1
        else:
            break
    print(count)
checkZero(number)