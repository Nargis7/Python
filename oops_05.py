class dog:
    species="canine" #class attribute
    def __init__(self,name,age): #constructor
        self.name=name
        self.age=age
# creating an object of the dog class
dog1= dog("buddy",3)
dog2= dog("charlie",5)
print(dog1.name)
print(dog1.age)
print(dog1.species)  #class variables
print(dog2.name)

# modify instance variables
dog1.name="max"
print(dog1.name)

# modify class variables
dog.species="feline"
print(dog1.species)  
