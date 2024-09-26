# lambda functions
# lambda functions are small anonymous functions
# they can take any number of arguments, but can only have one expression
# they are used to perform a small operation, like a function, but are defined inline
def summary(number,string):
    print(number*string)
summary(100,"I wish I would know this when I was a child")
def calculate(num1,num2):
    return [num1+num2,num1*num2,num1-num2,num1/num2,num1//num2,num1%num2,num1**num2]
print(calculate(10,5)) # returns a tuple of results
# In python, functions can return multiple values with one return
def main():
    summary(20,"Hello")
    print(calculate(10,5))