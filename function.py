# funcion is a block of code that perform particular task
def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum
cal_sum(2,3)    

def print_hello():
    print("hello")
print_hello()    

def cal_sum(a,b):
    return a+b
sum=cal_sum(23,45)
print(sum) 
# calcuate average of three numbers
def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
cal_avg(2,3,4)    

# write a function to print the length of a list(list in parameter)
cities=["delhi","jamshedpur","pune","mumbai","kolkata","noida","gurgaon"]
heroes=["thor","shaktiman","ironman","captain america"]
def print_len(list):
    print(len(list))
print_len(cities) 
print_len(heroes)

# write a function to print the elements of a list in a single line(list is the parameter)
heroes=["thor","shaktiman","ironman","captain america"]
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(heroes)
print_list(cities)        

# write a function to find the factorial of n
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
cal_fact(5)        
# write a function to convert usd to inr
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"usd=",inr_val,"inr")
converter(2)    
