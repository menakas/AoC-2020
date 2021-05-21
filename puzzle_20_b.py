import sys
import copy
import pprint

def try_all(tid1,edge,x,y):
	if edge == 0:
		func = has_left_match
	if edge == 1:
		func = has_top_match
	if edge == 2:
		func = has_right_match
	if edge == 3:
		func = has_bottom_match
	side = 0
	lst = list(match_set[tid1])
	for item in lst:
		rot = 0
		hflip = 0
		vflip = 0
		while not side:
			if not func(tid1,item):
				rotate_clock(item)
				rot +=1
				if rot>=4:
					if vflip:
						break
					if hflip:
						flip_ver(item)
						vflip=1
						rot = 0
					else:
						flip_hor(item)
						hflip = 1
						rot = 0
			else:
				side = item
				match_set[tid1].remove(item)
				match_set[item].remove(tid1)
				if edge == 0:
					matrix[x][y-1] = item
					set_neighbours(item,x,y-1)
				if edge == 1:
					matrix[x-1][y] = item
					set_neighbours(item,x-1,y)
				if edge == 2:
					matrix[x][y+1] = item
					set_neighbours(item,x,y+1)
				if edge == 3:
					matrix[x+1][y] = item
					set_neighbours(item,x+1,y)
				break

def set_neighbours(tid1,x,y):
	global mnx,mny
	global mxx,mxy
	if y< mny:
		mny = y
	if y> mxy:
		mxy = y
	if x< mnx:
		mnx = x
	if x> mxx:
		mxx = x
	print(tid1,x,y)
	try_all(tid1,0,x,y)
	try_all(tid1,1,x,y)
	try_all(tid1,2,x,y)
	try_all(tid1,3,x,y)

def has_top_match(tid1,tid2):
	target = tiles[tid1]
	other = tiles[tid2]
	match = 1
	for i in range(ln):
		if target[0][i] != other[ln-1][i]:
			match = 0
	return match
			
def has_bottom_match(tid1,tid2):
	target = tiles[tid1]
	other = tiles[tid2]
	match = 1
	for i in range(ln):
		if target[ln-1][i] != other[0][i]:
			match = 0
	return match
			
def has_left_match(tid1,tid2):
	target = tiles[tid1]
	other = tiles[tid2]
	match = 1
	for i in range(ln):
		if target[i][0] != other[i][ln-1]:
			match = 0
	return match
			
def has_right_match(tid1,tid2):
	target = tiles[tid1]
	other = tiles[tid2]
	match = 1
	for i in range(ln):
		if target[i][ln-1] != other[i][0]:
			match = 0
	return match
			

def rotate_clock(tid):
	target = tiles[tid]
	new = [['.' for k in range(ln)] for j in range(ln)]
	for i in range(len(target)):
		for j in range(len(target)):
			new[j][ln-1-i] = target[i][j]
	tiles[tid] = new.copy()

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
	if match_l or match_r or match_t or match_b:
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
	if match_l or match_r or match_t or match_b:
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
	if match_l or match_r or match_t or match_b:
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
	if match_l or match_r or match_t or match_b:
		return 1
				
	return 0 

def rotate_c():
	global final
	lng = len(final)
	new = [['.' for k in range(lng)] for j in range(lng)]
	for i in range(lng):
		for j in range(lng):
			new[j][lng-1-i] = final[i][j]
	final = new.copy()

def h_flip():
	global final
	lng = len(final)
	new = [['.' for k in range(lng)] for j in range(lng)]
	for i in range(lng):
		for j in range(lng):
			new[i][j] = final[lng-1-i][j]
	final = new.copy()

def v_flip():
	global final
	lng = len(final)
	new = [['.' for k in range(lng)] for j in range(lng)]
	for i in range(lng):
		for j in range(lng):
			new[i][j] = final[i][lng-1-j]
	final = new.copy()

def find_monsters():
	global final
	mct = 0
	for i in range(len(final)):
		for j in range(len(final)):
			found = 1
			for item in mset:
				if i+item[0] >= len(final) or j+item[1] >= len(final) or final[i+item[0]][j+item[1]] == '.':
					found = 0
					break
			if found:
				for item in mset:
					final[i+item[0]][j+item[1]] = 'O'
				
				mct +=1
	return mct

					
 
tid = 0
tiles = {}
first = 1
ln = 0
i=0

matrix = []
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

matrix = [['.' for k in range(ln*2)] for j in range(ln*2)]
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
				matches.add(other)
				ct+=1
			else:
				flip_hor(other)
				flip_ver(other)
				if has_matching_edges(item,other):
					matches.add(other)
					ct+=1
				else:
					flip_ver(other)
	for match in matches:
		match_set[item].add(match)
		match_set[match].add(item)

pprint.pprint((match_set))

more = set()
for tile in match_set:	
	more.add(tile)
	if len(match_set[tile]) == 4:
		current = tile

x = ln
y = ln
mnx = x
mxx = x
mny = y
mxy = y
matrix[x][y] = current
set_neighbours(current,x,y)	

print(mnx,mxx,mny,mxy)
lng = mxy+1-mny


pprint.pprint(tiles[matrix[9][9]])

monster = []
monster.append(list('                  # '))
monster.append(list('#    ##    ##    ###'))
monster.append(list(' #  #  #  #  #  #   '))


mset = set()
for i in range(len(monster)):
	for j in range(len(monster[i])):
		if monster[i][j] == '#':
			mset.add((i,j))

print(mset)

final = [['.' for k in range(lng*(ln-2))] for j in range(lng*(ln-2))]
a=0
b=0
for j in range(mnx,mxx+1):
	for h in range(1,ln-1):
		for k in range(mny,mxy+1):
			for i in range(1,ln-1):
				#print(a,b,j,k,h,i)
				final[a][b] = tiles[matrix[j][k]][h][i]
				b+=1
		a+=1
		b = 0

print(final)

rot = 0
hflip = 0
vflip = 0
mct = find_monsters()
while not mct and rot <4:
	rotate_c()
	print("rotate",rot,"vflip",vflip,"hflip",hflip)
	if rot >=4:
		if vflip:
			break;
		elif hflip:
			v_flip()
			vflip = 1
			rot =0
		else:
			h_flip()
			hflip = 1
			rot = 0
	rot+=1
	print(final)
	mct = find_monsters()

print(mct)

total = 0
for i in range(len(final)):
	for j in range(len(final)):
		if final[i][j] == '#':
			total +=1
print(final)
print(total)	
	
