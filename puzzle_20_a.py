import sys
import copy
import pprint


def flip_hor(tid):
	target = tiles[tid]
	new = [['.' for k in range(ln)] for j in range(ln)]
	for i in range(len(target)):
		for j in range(len(target)):
			new[i][j] = target[ln-1-i][j]
	tiles[tid] = new.copy()

def flip_ver(tid):
	target = tiles[tid]
	new = [['.' for k in range(ln)] for j in range(ln)]
	for i in range(len(target)):
		for j in range(len(target)):
			new[i][j] = target[i][ln-1-j]
	tiles[tid] = new.copy()

def has_matching_edges(tid1,tid2):
	target = tiles[tid1]
	other = tiles[tid2]
	ct = 0
	#print(tid1,tid2)
	# 0 , vary
	match_l = 1
	match_r = 1
	match_t = 1
	match_b = 1
	for j in range(len(target)):
		if target[0][j] != other[0][j]:
			match_t = 0
		if target[0][j] != other[ln-1][j]:
			match_b = 0
		if target[0][j] != other[j][0]:
			match_l = 0
		if target[0][j] != other[j][ln-1]:
			match_r = 0
	if match_l:
		return 1
	if match_r:
		return 1
	if match_t:
		return 1
	if match_b:
		return 1
				
	# ln-1 , vary
	match_l = 1
	match_r = 1
	match_t = 1
	match_b = 1
	for j in range(len(target)):
		if target[ln-1][j] != other[0][j]:
			match_t = 0
		if target[ln-1][j] != other[ln-1][j]:
			match_b = 0
		if target[ln-1][j] != other[j][0]:
			match_l = 0
		if target[ln-1][j] != other[j][ln-1]:
			match_r = 0
	if match_l:
		return 1
	if match_r:
		return 1
	if match_t:
		return 1
	if match_b:
		return 1
				
	# vary , 0
	match_l = 1
	match_r = 1
	match_t = 1
	match_b = 1
	for j in range(len(target)):
		if target[j][0] != other[0][j]:
			match_t = 0
		if target[j][0] != other[ln-1][j]:
			match_b = 0
		if target[j][0] != other[j][0]:
			match_l = 0
		if target[j][0] != other[j][ln-1]:
			match_r = 0
	if match_l:
		return 1
	if match_r:
		return 1
	if match_t:
		return 1
	if match_b:
		return 1

	# vary , ln-1
	match_l = 1
	match_r = 1
	match_t = 1
	match_b = 1
	for j in range(len(target)):
		#print(target[j][ln-1])
		if target[j][ln-1] != other[0][j]:
			match_t = 0
		if target[j][ln-1] != other[ln-1][j]:
			match_b = 0
		if target[j][ln-1] != other[j][0]:
			match_l = 0
		if target[j][ln-1] != other[j][ln-1]:
			match_r = 0
	if match_l:
		return 1
	if match_r:
		return 1
	if match_t:
		return 1
	if match_b:
		return 1
				
	return 0 
			
 
tid = 0
tiles = {}
first = 1
ln = 0
i=0

match_set = {}
for line in sys.stdin:
	line = line.strip()
	if not line:
		continue
	if "Tile" in line:
		(tile,tid) = line.split(' ')
		tid = tid[:-1]
		i = 0
		match_set[tid] = 0
		continue
	elif first:
		first = 0
		ln = len(line)
	if not i:
		tiles[tid] = []
	tiles[tid].append(list(line))
	i +=1

#pprint.pprint(tiles)

for item in tiles:
	ct = 0
	matches = set()
	if not match_set[item]:
		match_set[item] = set()
	for other in tiles:
		if not match_set[other]:
			match_set[other] = set()
		if item == other:
			continue
		if has_matching_edges(item,other):
			##print("Match")
			matches.add(other)
			ct+=1
		else:
			flip_hor(other)
			if has_matching_edges(item,other):
				#print("After flip hor Match")
				matches.add(other)
				ct+=1
			else:
				flip_hor(other)
				flip_ver(other)
				if has_matching_edges(item,other):
					#print("Match after vertical flip")
					matches.add(other)
					ct+=1
				else:
					flip_ver(other)
	for match in matches:
		match_set[item].add(match)
		match_set[match].add(item)

pprint.pprint((match_set))

product = 1
for tile in match_set:	
	if len(match_set[tile]) == 2:
		print(tile)
		product *= int(tile)


print(product)
