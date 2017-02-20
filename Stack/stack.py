
top=-1
st=[]
def delete(top):
	if top == (-1):
		print 'Stack is Empty.'
		return 
	p = st.pop()
	print 'Popped element is', p
	top = top - 1 
	return top
def insert(val, top, size):
	if top == size-1:
		print 'Stack Overflow. Please Try Again.'
		print 'Your Stack is :',st
		exit()
	st.append(val)
	top = top + 1
	return top

size = int(raw_input("Enter Size of the stack: ")) 
top=insert(34, top, size)
top=insert(47, top, size)
print st, top
top=delete(top)
top=insert(4, top, size)
top=insert(37, top, size)	
top=delete(top)
print st, top
top=delete(top)
print st, top
top=insert(344, top, size)
print st, top		
