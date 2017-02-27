#Quick Sort implementation
lst = raw_input('Enter list:')

#Split the raw input string and put the float values into the list.
lst = lst.split(' ')
val = []
val = [float(i) for i in lst]

#Quick Sort Algorithm (My favourite.)
#Program to sort a list in ascending order. 
def partition(val, l, h):
    pivot = val[h]
    pi = l-1
    for i in range(l, h):
        if val[i] <= pivot:
            pi = pi+1
            #Swap val[pi] and val[i]
            val[pi], val[i] = val[i], val[pi]
    pi = pi+1
    val[pi], val[h] = val[h], val[pi]
    return pi

def quick_sort(val, l, h):
    if l<h:
        p_index = partition(val, l, h)
        quick_sort(val, l, p_index-1)
        quick_sort(val, p_index+1, h)
#Call quick_sort function to sort the list.
quick_sort(val, 0, len(val)-1)
#Print sorted list.
print 'Sorted list : ',val
