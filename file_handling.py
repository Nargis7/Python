# age=input("enter your age:")
# f=open("data.txt",'w')
# f.write(age)
# f.close()
# f=open("data.txt",'r')
# print(f.read())
# f.close()

# f=open("hello.txt",'w')
# if f:
#     print("file successfully opened")
# print(type(f))    

# f=open("hello.txt",mode='w',buffering=10)
# if f:
#     print("opened")
# print(f) 

# f=open("hello.txt",mode='r')
# print(f.readable())
# print(f.writable())
# f.close()
# read mode
f=open("hello.txt",mode='r')
data=f.readlines() #size is optional
# data1=f.readline() #size is optional
for line in data:
    print(line,end="")
# print(data)
# print(data1)
f.close()
# binary mode
# f=open("hello.txt",mode='rb')
# data1=f.read()
# print(data1)
# f.close()
