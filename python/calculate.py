a=input("1st number")
a=int(a)
b=input("2nd number")
b=int(b)
print("enter the operation")
ch=str(input("enter specific operation +,-,*,/ :"))
result = 0
if ch =="+":
   result=a+b
elif ch == "-":
     result= a-b
elif ch =="*":
     result= a*b
elif ch =="/":
     result= a/b
else :
     print("sorry")
print(a,ch,b,":",result)
