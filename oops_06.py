class employee:
    def __init__(self,sal,age):
        self.salary=sal
        self.age=age
    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")
e1=employee(24000,21)            
e2=employee(34000,25)     

print(e1.salary)
e1.salary=45000
print(e1.salary)

e1.display()