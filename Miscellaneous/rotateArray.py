'''
Program to rotate array left or right by d elements.
'''
#Get the user input from raw_input()
inp = raw_input().split(' ')
#Extract n (number of values in array) and d (rotate array by this value) from inp list of strings. 
n,d = int(inp[0]), int(inp[1])

arr = raw_input().split(' ')
#Convert each string to int in the list 'arr'
arr = [int(i) for i in arr]
#Example : n = 12, d=3, arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#Function to find Greatest Common Divisor of a and b.
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b, a%b)
		
#Function to rotate array arr left by d elements. 
#For Example: for above data after completition of this function arr will be : arr = [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]
def rotateLeft(arr, n, d):
    for i in range(0, gcd(n, d)):
        temp = arr[i]
        j = i
        while(1):
            k = j+d
            if k>=n:
                k = k-n
            if k==i: 
                break
            arr[j] = arr[k]
            j=k
        arr[j]=temp

#Function to rotate array right arr by d elements. 
#For Example: for above data after completition of this function arr will be : arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def rotateRight(arr, n, d):
    for i in range(0, gcd(n,d)):
        temp = arr[n-1-i]
        j = n-1-i
        t = j
        while(1):
            k = j-d
            if k<0:
                k = k+n
            if k==t: 
                break
            arr[j] = arr[k]
            j=k
        arr[j]=temp

print arr
rotateLeft(arr, n, d)
print arr
rotateRight(arr, n, d)
print arr
