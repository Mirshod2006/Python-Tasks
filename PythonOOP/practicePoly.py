class Animal:
    def __init__(self,name):
        self.name = name
        pass
    def voice(self):
        pass

class Dog(Animal):
    def voice(self):
        return "Waow Waow Waow"
    
class Cat(Animal):
    def voice(self):
        return "Meow Meow Meow"
    
Tomas=Cat("Thomas")
print(Tomas.voice())
Bulldog = Dog("Ronald")
print(Bulldog.voice())


class Duck:
    def sound(self):
        return "Quack!"

class Wolf:
    def sound(self):
        return "Woof"

def animal_sound(animal):
    print(animal.sound())

duck = Duck()
dog = Wolf()

animal_sound(duck)  # Output: Quack!
animal_sound(dog)   # Output: Woof!

class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(2, 3))       # Output: 5
print(calc.add(2, 3, 4, 5)) # Output: 14

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(f"({p3.x}, {p3.y})")  # Output: (4, 6)