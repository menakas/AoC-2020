import sys

# A linked list node
class Node:
 
	# Constructor to create a new node
	def __init__(self, data):
		self.data = 'white'
		self.e = None
		self.ne = None
		self.se = None
		self.w = None
		self.nw = None
		self.sw = None
 
	def tile_exists(self, dirn):
		if dirn == 'w':
			if self.w:
				return 1
			elif self.nw and self.nw.sw:
				self.w = self.nw.sw
				self.w.e = self
				return 1
			elif self.sw and self.sw.nw:
				self.w = self.sw.nw
				self.w.e = self
				return 1
			else:
				return 0
		if dirn == 'e':
			if self.e:
				return 1
			elif self.ne and self.ne.se:
				self.e = self.ne.se
				self.e.w = self
				return 1
			elif self.se and self.se.ne:
				self.e = self.se.ne
				self.e.w = self
				return 1
			else:
				return 0
		if dirn == 'nw':
			if self.nw:
				return 1
			elif self.ne and self.ne.w:
				self.nw = self.ne.w
				self.nw.se = self
				return 1
			elif self.w and self.w.ne:
				self.nw = self.w.ne
				self.nw.se = self
				return 1
			else:
				return 0
		if dirn == 'ne':
			if self.ne:
				return 1
			elif self.e and self.e.nw:
				self.ne = self.e.nw
				self.ne.sw = self
				return 1
			elif self.nw and self.nw.e:
				self.ne = self.nw.e
				self.ne.sw = self
				return 1
			else:
				return 0
		if dirn == 'sw':
			if self.sw:
				return 1
			elif self.w and self.w.se:
				self.sw = self.w.se
				self.sw.ne = self
				return 1
			elif self.se and self.se.w:
				self.sw = self.se.w
				self.sw.ne = self
				return 1
			else:
				return 0
		if dirn == 'se':
			if self.se:
				return 1
			elif self.e and self.e.sw:
				self.se = self.e.sw
				self.se.nw = self
				return 1
			elif self.sw and self.sw.e:
				self.se = self.sw.e
				self.se.nw = self
				return 1
			else:
				return 0
	# Given a node as prev_node, insert a new node at dir
	def insertAt(self, tiles, dirn, new_data):

		new_node = Node(new_data)

		if dirn == 'e':
			self.e = new_node
			new_node.w = self
			if self.ne:
				self.ne.se = new_node
				new_node.nw = self.ne
				if self.ne.e:
					self.ne.e.sw = new_node
					new_node.ne = self.ne.e
					if self.ne.e.se:
						self.ne.e.se.w = new_node
						new_node.e = self.ne.e.se
			if self.se:
				self.se.ne = new_node
				new_node.sw = self.se
				if self.se.e:
					self.se.e.nw = new_node
					new_node.se = self.se.e
					if self.se.e.ne:
						self.se.e.ne.w = new_node
						new_node.e = self.se.e.ne

		if dirn == 'w':
			self.w = new_node
			new_node.e = self
			if self.nw:
				self.nw.sw = new_node
				new_node.ne = self.nw
				if self.nw.w:
					self.nw.w.se = new_node
					new_node.nw = self.nw.w
					if self.nw.w.sw:
						self.nw.w.sw.e = new_node
						new_node.w = self.nw.w.sw
			if self.sw:
				self.sw.nw = new_node
				new_node.se = self.sw
				if self.sw.w:
					self.sw.w.ne = new_node
					new_node.nw = self.sw.w
					if self.sw.w.nw:
						self.sw.w.nw.e = new_node
						new_node.w = self.sw.w.nw

		if dirn == 'ne':
			self.ne = new_node
			new_node.sw = self
			if self.nw:
				self.nw.e = new_node
				new_node.e = self.nw
				if self.nw.ne:
					self.nw.ne.sw = new_node
					new_node.nw = self.nw.ne
					if self.nw.ne.e:
						self.nw.ne.e.sw = new_node
						new_node.ne = self.nw.ne.e
			if self.e:
				self.e.nw = new_node
				new_node.se = self.e
				if self.e.ne:
					self.e.ne.w = new_node
					new_node.e = self.e.ne
					if self.e.ne.nw:
						self.e.ne.nw.sw = new_node
						new_node.ne = self.e.ne.nw

		if dirn == 'nw':
			self.nw = new_node
			new_node.se = self
			if self.ne:
				self.ne.w = new_node
				new_node.e = self.ne
				if self.ne.nw:
					self.ne.nw.sw = new_node
					new_node.ne = self.ne.nw
					if self.ne.nw.w:
						self.ne.nw.w.se = new_node
						new_node.nw = self.ne.nw.w
			if self.w:
				self.w.ne = new_node
				new_node.sw = self.w
				if self.w.nw:
					self.w.nw.e = new_node
					new_node.w = self.w.nw
					if self.w.nw.ne:
						self.w.nw.ne.se = new_node
						new_node.nw = self.w.nw.ne

		if dirn == 'se':
			self.se = new_node
			new_node.nw = self
			if self.sw:
				self.sw.e = new_node
				new_node.w = self.sw
				if self.sw.se:
					self.sw.se.ne = new_node
					new_node.sw = self.sw.se
					if self.sw.se.e:
						self.sw.se.e.nw = new_node
						new_node.se = self.sw.se.e
			if self.e:
				self.e.sw = new_node
				new_node.ne = self.e
				if self.e.se:
					self.e.se.w = new_node
					new_node.e = self.e.se
					if self.e.se.sw:
						self.e.se.sw.nw = new_node
						new_node.se = self.e.se.sw

		if dirn == 'sw':
			self.sw = new_node
			new_node.ne = self
			if self.se:
				self.se.w = new_node
				new_node.e = self.se
				if self.se.sw:
					self.se.sw.nw = new_node
					new_node.se = self.se.sw
					if self.se.sw.w:
						self.se.sw.w.ne = new_node
						new_node.sw = self.se.sw.w
			if self.w:
				self.w.se = new_node
				new_node.nw = self.w
				if self.w.sw:
					self.w.sw.e = new_node
					new_node.w = self.w.sw
					if self.w.sw.se:
						self.w.sw.se.ne = new_node
						new_node.sw = self.w.sw.se
		tiles.D[new_node] = 'white'


	def moveto(self, dirn):
		if dirn == 'w':
			return self.w
		if dirn == 'e':
			return self.e
		if dirn == 'nw':
			return self.nw
		if dirn == 'ne':
			return self.ne
		if dirn == 'sw':
			return self.sw
		if dirn == 'se':
			return self.se
 
	def flip(self, tiles):
		if self.data == 'white':
			print("Flipping to black",self)
			self.data = 'black'
			tiles.D[self] = 'black'
		elif self.data == 'black':
			print("Flipping to WHITE",self)
			self.data = 'white'
			tiles.D[self] = 'white'
		else:
			print("Ayyo")

 

# Class to create a HexGrid
class HexGrid:
 
	# Constructor for empty HexGrid
	def __init__(self):
		self.head = None
		self.D = {}
 
tiles =  HexGrid()
first = 1
for line in sys.stdin:
	line = line.strip()
	index = 0
	if first:
		tiles.head = Node('white')
		tiles.D[tiles.head] = 'white'
		first = 0
		current = tiles.head
	print(line)
	while (index < len(line)):
		if line[index] in 'ns':
			dirn = line[index:index+2]
			index +=2
		else:
			dirn = line[index:index+1]
			index +=1
		print(dirn)
		if not current.tile_exists(dirn):
			current.insertAt(tiles,dirn,'white')
			#print(current,"Whitenning")
		current = current.moveto(dirn)	
	current.flip(tiles)
	print(tiles.D)
total = 0
for item in tiles.D:
	if tiles.D[item] == 'black':
		total +=1
print(total)
		

