# and or not
# > < <= >= == !=
# == is used for equality check
# != is used for inequality check
# > and < are used for greater than and less than check respectively
# >= and <= are used for greater than or equal to and less than or equal to check respectively
# In Python, we can use the following operators for comparison:
#   - Equal to: a == b
#   - Not equal to: a != b
#   - Greater than: a > b
#   - Less than: a < b
#   - Greater than or equal to: a >= b
#   - Less than or equal to: a <= b
#   - is: used to check if both variables point to the same object in memory
#   - is not: used to check if both variables do not point to the same object in
#   memory
#   - in: used to check if a value is present in a sequence (like a list
#   or a string)
#   - not in: used to check if a value is not present in a sequence (like
#   a list or a string)
#   - and: used to check if both conditions are true
#   - or: used to check if at least one condition is true
#   - not: used to check if a condition is false
#   - in operator is used to check if a value is present in a sequence (like a
#   list or a string)
#   - not in operator is used to check if a value is not present in a sequence (
#   like a list or a string)
#   - in operator is used to check if a value is present in a sequence (like a
#   list or a string)
#   - not in operator is used to check if a value is not present in a sequence (
#   like a list or a string)   
a = int(input("Enter number to analyse it:"))
if a>0:
    print("Number is positive")
elif a==0:
    print("Number is null")
else:
    print("Number is negative")


if a%2==0:
    print("Number is even")
else:
    print("Number is odd")
prime = True
for i in range(2,a-1):
    if a%i==0:
        print("Number is not prime")
        prime = prime & False
        break
if(prime):
    print("Number is prime")
