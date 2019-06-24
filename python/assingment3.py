def leftRotate(arr, d, n): 
	for i in range(d): 
		leftRotatebyOne(arr, n) 
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i + 1] 
	arr[n-1] = temp 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d"% arr[i], end =" ")     
arr = [1, 2, 3, 4, 5] 
print(arr)
leftRotate(arr, 1, 5) 
printArray(arr, 5) 
#shift 1
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i + 1] 
	arr[n-1] = temp 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d"% arr[i], end =" ")     
arr = [1, 2, 3, 4, 5] 
print(arr)
leftRotate(arr, 2, 5) 
printArray(arr, 5) 
#SHIFT 2
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i + 1] 
	arr[n-1] = temp 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d"% arr[i], end =" ")     
arr = [1, 2, 3, 4, 5] 
print(arr)
leftRotate(arr, 3, 5) 
printArray(arr, 5) 
#SHIFT 3
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i + 1] 
	arr[n-1] = temp 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d"% arr[i], end =" ")     
arr = [1, 2, 3, 4, 5] 
print(arr)
leftRotate(arr, 4, 5) 
printArray(arr, 5) 
#SHIFT 4
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i + 1] 
	arr[n-1] = temp 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d"% arr[i], end =" ")     
arr = [1, 2, 3, 4, 5] 
print(arr)
leftRotate(arr, 5, 5) 
printArray(arr ,5) 
#SHIFT 5 AND RETURN 1 AGAIN