import sys 


mx = 1200000
first =0
buses = []
matrix = []
for i in range(mx):
    matrix.append('.')
for line in sys.stdin:
    line = line.strip()
    if first:
        buses = line.split(',')
    else:
        busid = int(line)
    first = 1

for i in range(len(buses)):
    print i,buses[i]

for i in range(len(buses)):
    if  buses[i] == 'x':
        continue
    j=0
    index = j* int(buses[i])
    while index < mx:
        matrix[index] = int(buses[i])
        j +=1
        index = j* int(buses[i])


for j in range(busid,mx):
    if matrix[j] != '.':
        print matrix[j],j, j- busid, int(matrix[j]) * (j-busid)
        break 
