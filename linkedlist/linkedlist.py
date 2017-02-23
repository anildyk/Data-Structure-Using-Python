#Make a node of the linked list
class Node:
	#Initialize a node object of the linked list.
	def __init__(self,data):
		self.data = data
		self.next = None


class LinkedList:
	#Initialize head with this function
	def __init__(self):
		self.head = None
	#Call this function on linked list to print the list 
	def printList(self):
		if self.head is None:
			print "Nothing to print. List is Empty."
			return
		print "Your list is : "
		temp = self.head
		while(temp):
			print temp.data
			temp = temp.next
	#Insert into the list 
	#Three ways to add a node to the linked list
	# 1. At the front of the list - insertAtFront()
	# 2. After a given node - insertAfterNode()
	# 3. At the end of the list - insertAtEnd()
	def insertAtFront(self, data):
		#Make a node and insert data
		newNode = Node(data)
		#Make next of newNode as head
		newNode.next = self.head
		#Make next of head as newNode
		self.head = newNode
	def insetAtEnd(self, data):
		#Make a node and insert data
		newNode = Node(data)
		#If list is empty then make newNode head of linked list and return
		if self.head is None:
			self.head = newNode
			return
		#Iterate through nodes till last node
		temp = self.head
		while(temp.next):
			temp = temp.next
		#Make newNode next node of the last node.
		temp.next = newNode
	def insertAfterNode(self, prev, data):
		if prev is None:
			print "This node is not in the LinkedList."
			return
		newNode = Node(data)
		#Make next of newNode as next of prev(given node) node 		
		newNode.next = prev.next
		#Make next of prev node as newNode
		prev.next = newNode
		
	def deleteNodeByKey(self, key):
		
		temp = self.head
		#If list is empty
		if temp is None:
			print 'Please insert something and then delete.'
			return
	
		#If head node's data is equal to key.
		if temp is not None:
			if temp.data == key:
				self.head = temp.next
				print 'Deleted node\'s value is', temp.data
				temp = None
				return
		while temp is not None:
			if temp.data == key:
				break
			prev = temp
			temp = temp.next
		
		prev.next = temp.next
		print 'Deleted node\'s value is', temp.data
		temp = None
	def deleteNodeByPosition(self, pos):
		temp = self.head
		if temp is None:
			print 'Nothing in the LinkedList.'
			return
		if pos==0:
			self.head = temp.next
			temp = None
			return		
		c=0
		while c < pos and temp is not None:
			temp = temp.next
			
		if temp is None or temp.next is None:
			return
		t = temp.next.next
		temp.next = None
		temp.next = t
			
			 


#Code execution starts here.
if __name__=='__main__':
	
	ll = LinkedList()
	
	ll.head = Node(7)
	
	second = Node(8)
	ll.head.next = second
	
	third = Node(9)
	second.next = third
		
	ll.printList()
	ll.insertAfterNode(second,343)
	ll.printList()
	ll.deleteNodeByKey(9)
	ll.printList()
	ll.deleteNodeByPosition(0)
	ll.printList()
