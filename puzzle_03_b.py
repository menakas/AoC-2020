import sys

treemap = []
for line in sys.stdin:
  line = line.strip()
  treemap.append(line)

lgth = len(treemap[0])

def get_num_trees(xin,yin):
	treecount=0
	x=0
	y=0
	while ( x < len(treemap) ):
	  if treemap[x][y] == '#':
	    treecount+=1
	  x +=xin
	  y +=yin
	  if y >= lgth:
	    y= y - lgth
	  if x >= len(treemap):
	   break
	return treecount


product = 1

product *= get_num_trees(1,1)
product *= get_num_trees(1,3)
product *= get_num_trees(1,5)
product *= get_num_trees(1,7)
product *= get_num_trees(2,1)

print(product)

