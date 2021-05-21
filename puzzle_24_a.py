import sys
import pprint


tiles = {}
first = 1
start = (0,0,0)
tiles[start] = 'white'
for line in sys.stdin:
	line = line.strip()
	index = 0
	print(line)
	current = start
	while (index < len(line)):
		if line[index] in 'ns':
			dirn = line[index:index+2]
			index +=2
		else:
			dirn = line[index:index+1]
			index +=1
		print(dirn)
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
		print(current)
	if tiles[current] == 'black':
		print("Flipping to WHITE",current)
		tiles[current] = 'white'
	elif tiles[current] == 'white':
		print("Flippong to black",current)
		tiles[current] = 'black'
	else:
		print("Ayyoo")
	pprint.pprint(tiles)

total = 0
for item in tiles:
	if tiles[item] == 'black':
		total +=1
print(total)
		

