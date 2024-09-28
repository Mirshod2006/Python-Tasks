try:
    print(10)
    print('1'+1)
    print(2/0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except TypeError:
    print("An error occurred")
    print("Hello World!")
except:
    print("An error occurred")

a,b = int(input("a=")),int(input("b="))
try:
    print(a/b)
    print(a*b)
    print(a//b)
    print(a%b)
except:
    print("During the execution of arithmetic operations!")
else:
    print("Xatolik Topilmadi!")
finally:
    print("At least, all is over!")

try:
    raise NameError("Nomini e'lon qilishdagi xatolik!")
    raise TypeError("Tipdagi xatolik")
except:
    print("Something in The world!")