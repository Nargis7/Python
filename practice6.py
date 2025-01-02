# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(4))   
# write a recursive function to calculate the sum of first n natural numbers
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1)+n
# print(calc_sum(5))    

# write a recursive function to print all elements in a list
# hints: use list and index as parameters
# def print_list(list,idx=0):
#     if (idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# fruits=["mango","litchi","banana","grapes","watermelon","apple"]
# print_list(fruits)        
# write a recursive function to print fibonacci sequence
def fibonacci(n):
    if(n<=1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))        