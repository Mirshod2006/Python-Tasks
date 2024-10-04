class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print(f"{self.name} has been deleted")

class Zombie(Human):
    pass

class Monster(Human):
    def __init__(self,name,age,health):
        super().__init__(name,age)
        self.health=health
    
    def health(self):
        if(self.health==0):
            self.health=100

class Professor_Naseer(Monster):
    def __init__(self,name,age,health,field,rank):
        super().__init__(name,age,health)
        self.field=field
        self.rank=rank

    def who(self):
        print("My name is professor ",self.name
              ," and I teach from ",self.field," and also",
              " I ranked in ",self.rank," in the world!",
              " and I am ",self.age," years old",
              " and I is always",self.health,"% healthy")
        
Naseer = Professor_Naseer("Naseer",50,100,"Operating Sysrems","5")
Naseer.who()