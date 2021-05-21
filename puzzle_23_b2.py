import sys

#inpt = '389125467'
inpt = '792845136'

# A linked list node
class Node:
 
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
 
# Class to create a Doubly Linked List
class DoublyLinkedList:
 
	# Constructor for empty Doubly Linked List
	def __init__(self):
		self.head = None
		self.D = {}
 
	# Given a node as prev_node, insert a new node after
	# the given node
	def insertAfter(self, prev_node, new_data):
 
		if prev_node is None:
			print "the given previous node cannot be NULL"
			return
 
		new_node = Node(new_data)
		self.D[new_data] = new_node
 
		new_node.next = prev_node.next
		prev_node.next = new_node
 
		new_node.prev = prev_node
		new_node.next.prev = new_node
 
	# Given a reference to the head of DLL and integer,
	# appends a new node at the end
	def append(self, new_data):
 
		new_node = Node(new_data)
		self.D[new_data] = new_node

		if self.head is None:
			self.head = new_node
			self.head.next = self.head
			self.head.prev = self.head
			return

		if self.head.prev is None:
			last = self.head
		else:
			last = self.head.prev
 
		last.next = new_node
		new_node.prev = last

		new_node.next = self.head
		self.head.prev = new_node
 
		return

	def pick3(self, current):
 
		three = [current.next.data,current.next.next.data,current.next.next.next.data]

		nextptr = current.next.next.next.next
		del current.next.next.next
		del current.next.next
		del current.next
		current.next = nextptr 
		current.next.prev = current
		return three
 

	def get_dest(self, label, three):
		dest = int(label) -1
		if dest == 0:
			dest = mx
		while str(dest) in three:
			dest -=1
			if dest == 0:
				dest = mx
		#print("Dest", str(dest))
		return self.D[str(dest)]
	
 
	# This function prints contents of linked list
	# starting from the given node
	def printList(self, node):
 
		start = node
		print "\nTraversal in forward direction"
		print " % s" %(node.data),
		node = node.next
		while(node is not start):
			print " % s" %(node.data),
			last = node
			node = node.next
		print()
 
 
 
mx = 1000000
moves = 10000000

mcount = 0
# Start with empty list
cups = DoublyLinkedList()

labels = list(inpt)
cups.head = Node(labels[0])
cups.D[labels[0]] = cups.head


for i in range(1,len(labels)):
	cups.append(labels[i])

for i in range(len(labels)+1,mx+1):
	cups.append(str(i))

#cups.printList(cups.head)

current = cups.head
while mcount < moves:
	if mcount %1000 == 0:
		print(mcount)
	#cups.printList(cups.head)
	three = cups.pick3(current)
	cups.head = current
	clabel = current.data
	destn = cups.get_dest(clabel,three)
	cups.insertAfter(destn,three[2])
	cups.insertAfter(destn,three[1])
	cups.insertAfter(destn,three[0])
	current = current.next
	mcount +=1

cups.printList(cups.head)

start = cups.D['1']
print(int(start.next.data) * int(start.next.next.data))

