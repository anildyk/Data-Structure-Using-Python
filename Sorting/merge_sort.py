#Merge Sort implementation
lst = raw_input('Enter list:')

#Split the raw input string and put the float values into the list.
lst = lst.split(' ')
val = []
val = [float(i) for i in lst]

#Merge sort Algorithm (My second favourite sorting algorithm.)
#Program to sort a list in ascending order. 
#Function to merge to sorted subarray val[l:m+1] ans val[m+1:h]
def merge(val, l, m, h):
    i=0
    j=0
    k=l
    a = []
    b = []
    a = val[l:m+1]
    b = val[m+1:h+1]
    while i < len(a) and j<len(b):
        if a[i] < b[j]:
            val[k] = a[i]
            i=i+1
        else:
            val[k] = b[j]
            j=j+1
        k = k+1
    while i < len(a):
        val[k] = a[i]
        k = k+1
        i=i+1
    while j < len(b):
        val[k] = b[j]
        k = k+1
        j = j+1
    return val
#Function to sort a list/array val from index l to h or
#Function to sort a sublist/subarray val[l:h+1]
def merge_sort(val, l, h):
    if l<h:
        mid = (l+h)/2
        merge_sort(val, l, mid)
        merge_sort(val, mid+1, h)
        merge(val, l, mid, h)

#Call merge_sort function to sort the given list i.e. val
merge_sort(val, 0, len(val)-1)
#Print sorted list.
print 'Sorted list : ',val
