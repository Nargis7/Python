# write a pyhton program to check if a number by the user is odd or even
# num=14
# num=int(input("enter a num:"))
# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")    

# write a pyhton program to find the greatest of 3 number entered by user
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if(a>=b and a>=c):
    print("first number is largest:",a)
elif(b>=c):
    print("first number is largest:",b)
else:
    print("third number is largest:",c)    