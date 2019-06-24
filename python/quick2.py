Array = [54,20,92,17,5,25]
low = 0
up = len(Array) - 1
 
def partition(Array,low,up):
	i = low+1
	j = up
	pivot = Array[low]
	while(i<=j):
		while(Array[i]<pivot and i<up):
			i = i+1
		while(Array[j]>pivot):
			j = j-1
		if(i<j):
			Array[i],Array[j] = Array[j],Array[i]
			i = i+1
			j = j-1
		else:
			i = i+1
	Array[low] = Array[j]
	Array[j] = pivot
	return j
 
def quick(Array,low,up):
	if(low>=up):
		return
	p = partition(Array,low,up)
	quick(Array,low,p-1)
	quick(Array,p+1,up)
 
quick(Array,low,up)
 
for i in Array:
	print (i)