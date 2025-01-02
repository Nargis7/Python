# creates student class that take name and marks of 3 subjects
#  as arguments in constructor then create a method to print
#  the average
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod #decorator
    def hello():
        print("hello")    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hii",self.name,"your avg score is",sum/3)        
s1=student("karan",[1,2,3]) 
s1.get_avg()
s1.hello()       
