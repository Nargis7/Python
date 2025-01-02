height=int(input("What is your height:"))
if height>=3:
    print("you can ride")
    age=int(input("What is your age:"))
    if age<=18:
        print("please pay 250Rs")
    elif age>=18:
        print("please pay 300Rs")
    else:
        print("please pay 500 Rs")        
else:
    print("can't ride")
print("bye")    