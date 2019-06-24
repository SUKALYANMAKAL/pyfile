list1 = [4, 3, 1, 10, 13, 5]
print "unsorted list",list1
for j in range (len(list1)-1):
    for i in range(len(list1)-1):       
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
        print "sorted list",list1