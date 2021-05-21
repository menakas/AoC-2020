import sys
import pprint
import copy


def add_adjacent(item):
	ct = 0
	if (item[0]+1,item[1],item[2]-1) not in tiles:
		tiles[(item[0]+1,item[1],item[2]-1)] = 'white'
	if (item[0]-1,item[1],item[2]+1) not in tiles:
		tiles[(item[0]-1,item[1],item[2]+1)] = 'white'
	if (item[0]+1,item[1]-1,item[2]) not in tiles:
		tiles[(item[0]+1,item[1]-1,item[2])] = 'white'
	if (item[0]-1,item[1]+1,item[2]) not in tiles:
		tiles[(item[0]-1,item[1]+1,item[2])] = 'white'
	if (item[0],item[1]+1,item[2]-1) not in tiles:
		tiles[(item[0],item[1]+1,item[2]-1)] = 'white'
	if (item[0],item[1]-1,item[2]+1) not in tiles:
		tiles[(item[0],item[1]-1,item[2]+1)] = 'white'

def get_count(item):
	ct = 0
	if (item[0]+1,item[1],item[2]-1) in tiles and tiles[(item[0]+1,item[1],item[2]-1)] == 'black':
		ct+=1
	if (item[0]-1,item[1],item[2]+1) in tiles and tiles[(item[0]-1,item[1],item[2]+1)] == 'black':
		ct+=1
	if (item[0]+1,item[1]-1,item[2]) in tiles and tiles[(item[0]+1,item[1]-1,item[2])] == 'black':
		ct+=1
	if (item[0]-1,item[1]+1,item[2]) in tiles and tiles[(item[0]-1,item[1]+1,item[2])] == 'black':
		ct+=1
	if (item[0],item[1]+1,item[2]-1) in tiles and tiles[(item[0],item[1]+1,item[2]-1)] == 'black':
		ct+=1
	if (item[0],item[1]-1,item[2]+1) in tiles and tiles[(item[0],item[1]-1,item[2]+1)] == 'black':
		ct+=1
	return ct

tiles = {}
first = 1
start = (0,0,0)
tiles[start] = 'white'


for line in sys.stdin:
	line = line.strip()
	index = 0
	current = start
	while (index < len(line)):
		if line[index] in 'ns':
			dirn = line[index:index+2]
			index +=2
		else:
			dirn = line[index:index+1]
			index +=1
		#print(dirn)
		if dirn == 'ne':
			current = (current[0]+1,current[1],current[2]-1)
		if dirn == 'sw':
			current = (current[0]-1,current[1],current[2]+1)
		if dirn == 'nw':
			current = (current[0],current[1]+1,current[2]-1)
		if dirn == 'se':
			current = (current[0],current[1]-1,current[2]+1)
		if dirn == 'e':
			current = (current[0]+1,current[1]-1,current[2])
		if dirn == 'w':
			current = (current[0]-1,current[1]+1,current[2])
		if current not in tiles:
			tiles[current] = 'white'
		#print(current)
	if tiles[current] == 'black':
		#print("Flipping to WHITE",current)
		tiles[current] = 'white'
	elif tiles[current] == 'white':
		#print("Flippong to black",current)
		tiles[current] = 'black'
		add_adjacent(current)
	else:
		print("Ayyoo")
	#pprint.pprint(tiles)


days = 100


day = 0

while day < days:
	new_tiles = {}
	#pprint.pprint(tiles)
	SEEN = set()
	Q = set(tiles.keys()) 
	while Q:
		item = Q.pop()
		#print(SEEN)
		#print(Q)
		ct = get_count(item)
		if tiles[item] == 'black' and (ct ==0 or ct > 2):
			new_tiles[item] = 'white'
		elif tiles[item] == 'white' and ct == 2:
			new_tiles[item] = 'black'
			add_adjacent(item)
		else:
			new_tiles[item] = tiles[item]
		SEEN.add(item)
		Q = set(tiles.keys()).difference(SEEN)

	day +=1
	tiles = new_tiles.copy()
	total = 0
	for item in tiles:
		if tiles[item] == 'black':
			total +=1
	print(day,total)
	

		

