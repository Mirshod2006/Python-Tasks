def fill_list(number):
    """Fill a list with numbers."""
    for i in range(int(input("n="))):
        number.append(input("--->"))
ls=[]
fill_list(ls)
#print(*ls)
def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#print(factorial(int(input("Enter number for factorial:"))))

def showReverse(number):
    """Show the reverse of a number."""
    if number>0:
        print(number%10,end=" ")
        showReverse(number//10)
    else:
        print()
showReverse(int(input("Enter number to show reverse:")))
def showInOrder(number):
    """Show the numbers in order from smallest to largest."""
    if number>0:
        showInOrder(number//10)
        print(number%10,end=" ")
showInOrder(int(input("Enter number to show in order:")))