size=(input("What size pizza you want(S/M/L)?"))
bill=0
if size == 'S' or size == 's':
    bill+=100
    print("small pizza price is 100rs.")
elif size == 'M' or size == 'm':
    bill+=200
    print("medium pizza price is 200rs.")
else:
    bill+=300
    print("large pizza price is 300rs.")  
add_pepperoni=input("Do you want pepperoni(Y/N)?")
if add_pepperoni == 'Y' or add_pepperoni== 'y':
    if size == 'S' or size == 's':
       bill+=30
    else:
       bill+=50
extra_cheese=input("Do you want extra cheese(Y/N)?")    
if extra_cheese == 'Y' or extra_cheese == y:
    bill+=20
print("your final bill is {bill}")    



