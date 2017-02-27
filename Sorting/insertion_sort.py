#Insertion Sort implementation
lst = raw_input('Enter list:')

#Split the raw input string and put the float values into the list.
lst = lst.split(' ')
val = []
val = [float(i) for i in lst]
#If you would like to sort a list of integers then replace "float(i)" with "int(i)" in the line above.

#Insertion sort Algorithm 
#Program to sort a list in ascending order.
#To sort in descending order: change "while j>= 0 and val[j] > temp :" to "while j>= 0 and val[j] < temp :"
for i in range(1, len(val)):
    temp = val[i]
    j=i-1
    while j>= 0 and val[j] > temp :
        val[j+1] = val[j]
        j = j-1
    val[j+1]=temp
#Print sorted list.
print 'Sorted list : ',val
