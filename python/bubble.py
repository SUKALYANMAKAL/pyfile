#list1 =int(input("enter the numbers :"))
list1  = [5, 6, 0, 1, 2, 4]
print ("unsorted list" , list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1):
      if list1[i] > list1[i+1]:
       list1[i],list1[i+1]=list1[i+1],list1[i]
     # else:
        # print list1
print ("sorted list",list1)