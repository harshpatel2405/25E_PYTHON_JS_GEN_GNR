# * name same , number of parameters same 

class Animal:
    def sound(self):
        print("Animal Makes Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

d = Dog()
c = Cat()

d.sound()
c.sound()