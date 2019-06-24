#define function (add two numbers):
def add(x, y):
    return x+ y
#define function (substruct two numbers):
def substruct(x, y):
    return x- y
#define function (multiply two numbers):
def multiply(x, y):
    return x* y
#define function (devide two numbers):
def divide(x, y):
    return(x/ y)
    print("select any operation ")
    print("1.Add")
    print("2.Sub")
    print("Multi")
    print("4.Div")
#take input in user:
choice = input("Enter choice(1/2/3/4/: )")
num1 = float(input("Enter the 1st number :"))
num2 = float(input("Enter the 2nd number :"))
if choice == '1':
    print(num1, "+", num2,"=", add(num1,num2))
elif choice == "2":
    print(num1, "-", num2,"=",substruct(num1,num2))
elif choice == "3":
    print(num1, "*", num2,"=",multiply(num1,num2))
elif choice == "4":
    print(num1, "/", num2,"=",divide(num1,num2))
else:
    print("invalid input ")
