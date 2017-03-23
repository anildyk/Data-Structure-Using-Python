'''Print below pattern using python
1
2 * 2
3 * 3 * 3
4 * 4 * 4 * 4
4 * 4 * 4 * 4
3 * 3 * 3
2 * 2
1
'''
'''
First loop will print this.
1
2 * 2
3 * 3 * 3
4 * 4 * 4 * 4
'''
for i in range(1,5):
	for j in range(0,i):
		if j==i-1:
			print(i)
		else:			
			print str(i)+' *',

'''
Loops given below will print this patern.
4 * 4 * 4 * 4
3 * 3 * 3
2 * 2
1
'''
for i in range(4,0,-1):
	for j in range(0,i):
		if j==i-1:
			print i
		else:
			print str(i)+' *',
	
