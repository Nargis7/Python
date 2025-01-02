# create a program that determine if a given entered by the user is a leap year
year=int(input("enter the number:"))
if(year%4==0 and year%100!=0):
  print("the year is leap year")
else:
    print("the year is not leap year")  