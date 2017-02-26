#Program to sort a list of float values using Bubble sort.
lst = raw_input('Enter you array or list:')
#Get all the values from raw string to a list of float values. 
lst = lst.split(' ')
values =[] 
values = [float(i) for i in val ]

#Sort the list "values" by Bubble Sort.
for i in range(0,len(values)):
  for j in range(0,len(values)-i-1):
    if values[j]>values[j+1]:
        values[j], values[j+1] = values[j+1], values[j]
        
#Print sorted list.
print values
