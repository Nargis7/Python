class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass  
class Dog(Animal):
    def speak_1(self):
        print("woof") 
class Cat(Animal):
    def speak_2(self):
        print("Meow!")
class DogCat(Dog,Cat):
    # pass
    def speak_3(self):
        print("This is child class")

a = DogCat("buddy")

print(a.name)
# print(animal.speak())
# print(a.speak_1())
# print(a.speak_2())
a.speak_1()
a.speak_2()
a.speak_3()