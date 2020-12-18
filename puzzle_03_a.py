import sys

treemap = []
for line in sys.stdin:
  line = line.strip()
  treemap.append(line)

lgth = len(treemap[0])

treecount=0
x=0
y=0
while ( x < len(treemap) ):
  if treemap[x][y] == '#':
    treecount+=1
  x +=1
  y +=3
  if y >= lgth:
    y= y - lgth
  if x >= len(treemap):
    print(treecount)
    exit()
  
