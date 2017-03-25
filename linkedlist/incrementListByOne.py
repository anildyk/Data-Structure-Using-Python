#Question : Add one to the number repesented by linked list with recursion.
#Linked list node.
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
#Linked List and its methods. 
class LinkedList:
	def __init__(self):
		self.head = None
  
	def printList(self):
		if self.head is None:
			return
		temp = self.head
		while temp.next:
			print str(temp.data)+"->",
			temp=temp.next
		print temp.data
	#Functio to add one to number denoted by linked list.
	def addOnetoList(self):
		#Call addOne function to add 1.
		carry = self.addOne(self.head)
		if carry==1:
			temp = Node(1)
			temp.next = self.head
	#Recursively call addOne to increment number by 1 which is denoted by linked list.
	def addOne(self, head):
		if not head:
			return 1
		res = head.data + self.addOne(head.next)
		#if head.data > 9 then we will replace that with res%10 and return carry by res/10.
		head.data = res%10
		return (res)/10
		

if __name__=='__main__':
	ll = LinkedList()	
	ll.head = Node(7)
	
	second = Node(8)
	ll.head.next = second
	
	third = Node(9)
	second.next = third
	#7->8->9 == 789
	#Adding one to it - 7->9->0
	ll.printList()
	ll.addOnetoList()
	ll.printList()
