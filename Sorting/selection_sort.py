#Sort a list of float values using Selection Sort
lst = raw_input('Enter list:')

#Split the raw input string and put the float values into the list.
lst = lst.split(' ')
val = []
val = [float(i) for i in lst]

#Selection sort Algorithm 
#Program to sort a list in ascending order.
#To sort in descending order: change "if val[j] < val[m]:" to "if val[j] > val[m]:" 
for i in range(0, len(val)):
    m = i
    for j in range(i+1, len(val)):
        if val[j] < val[m]:
            m=j
    if m != i:
        val[i], val[m] = val[m], val[i]
#Print sorted list.
print val
