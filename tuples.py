# tup=(78,89,90,45,23)
# print(type(tup))
# print(tup[4])
# print(tup)
# write a program to ask a user to enter three movies and store them in a list 
# movies=[]
# mov1=input("enter first movie:")
# mov2=input("enter second movie:")
# mov3=input("enter third movie:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# write a program to check if a list contain palindrome element
# list1=[1,2,1]
# copy_list1=list1.copy()
# copy_list1.reverse()
# if(copy_list1==list1):
#     print("palindrome")
# else:
#     print("not palindrome")    
str=input("enter the string:")
if str==str[::-1]:
   print("The string is palindrome")
else:
    print("The string is not palindrome")   