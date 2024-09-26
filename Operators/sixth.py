num1 = int(input("Enter the first num:"))
num2 = int(input("Enter the second num:"))
if num1>=num2:
    if num1%num2==0:
        print(True)
    else:
        print(False)
else:
    if num2%num1==0:
        print(True)
    else:
        print(False)