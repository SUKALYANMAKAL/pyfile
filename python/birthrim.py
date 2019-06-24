dict = {}
while True:
    print("       Birthday Reminder app        ")
    print("1.Date of Birth")
    print("2.Add the birthday list")
    print("3.exit")
    choice =int(input("enter your choice :"))
    if choice == 1:
        if len(dict.keys())==0:
            print("nothing is here ")
        else:
            name=input("enter the name look for birthday ")
            birthday=dict.get(name,"nothing found")
            print(birthday)
    elif   choice == 2:
        name=input("enter the name :")
        date=input("enter the date :")
        dict[name]=date
        print("birthday is added")
    elif choice==3:
        break
    else:
            print("invalid option")
            print("select a valid option")
        