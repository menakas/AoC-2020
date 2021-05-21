import sys 


first = 0
for line in sys.stdin:
    line = line.strip()
    if first:
        buses = line.split(',')
    first = 1

#https://www.dcode.fr/chinese-remainder
for i in range(0,len(buses)):
    if buses[i] != 'x':
         print int(buses[i])-i,int(buses[i]) 
