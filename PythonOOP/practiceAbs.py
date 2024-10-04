from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def speed(self):
        pass

class Tesla(Car):
    def speed(self):
        return 150
    def self_drive():
        return True
    
class Ferrari(Car):
    def speed(self):
        return 200
    def stable(self):
        return True