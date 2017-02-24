import Queue
class Node:
	
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def inorder(root):
	if root is None:
		return
	else:
		inorder(root.left)
		print ' ',root.data
		inorder(root.right)
def preorder(root):
	if root:
		print root.data
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root is None:
		return 
	else:
		postorder(root.left)
		postorder(root.right)
		print root.data
#q = Queue.Queue()
q = []
def levelorderIter(root):
	if root:
		q.append(root)
		while len(q)>0:
			node = q.pop(0)
			print node.data
			if node.left: q.append(node.left)
			if node.right: q.append(node.right)
q1=[]
def printLevel(root, l):
	if root:
		if l==1:
			print root.data
		elif l>1:
			printLevel(root.left, l-1)
			printLevel(root.right, l-1)
			
def levelorderRec(root):
	h = height(root)
	for i in range(1,h+1):
		printLevel(root, i)
		
def height(root):
	if root is None:
		return 0
	else:
		lh = height(root.left)
		rh = height(root.right)
		
		if lh>rh:
			return lh+1
		else:
			return rh+1
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(5)
root.left.right = Node(13)
root.right.left = Node(17)
root.right.right = Node(25)

print 'Inorder treversal of the BST is :',inorder(root)
print 'Preorder traversal of the BST is :', preorder(root)
print 'Postorder traversal of the BST is', postorder(root)
print 'Levelorder traversal (by Iterative approach)of the BST is', levelorderIter(root)
print 'Levelorder traversal (by Recursive approach)of the BST is', levelorderRec(root)
print 'Height of the Binary Search Tree is', height(root)

