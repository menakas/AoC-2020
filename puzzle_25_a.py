import sys

def transform(sub,loop):
	val = 1
	for i in range(loop):
		val = val*sub
		val = val % 20201227
	return val

def get_loop(sub,num):
	val = 1
	l = 0
	while val != num:
		val = val*sub
		val = val % 20201227
		l +=1
	return l


first =1
cpk = 0
dpk = 0
for line in sys.stdin:
	if first:
		cpk = int(line.strip())
		first = 0
	else:
		dpk = int(line.strip())

cloop = get_loop(7,cpk)
dloop = get_loop(7,dpk)
print(cloop,dloop)

cekey = transform(cpk,dloop)
dekey = transform(dpk,cloop)
print(cekey,dekey)
