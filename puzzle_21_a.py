import sys
import pprint

al2in = {}
allstr = ''
remain = set()
ct = 0
for line in sys.stdin:
	line = line.strip()
	line = line.rstrip(")")
	(instr,alstr) = line.split(" (contains ")
	allstr += ' ' + instr
	allist = alstr.split(", ")
	for al in allist:
		if al not in al2in:
			al2in[al] = []
		al2in[al].append(set(instr.split(' ')))

allstr = allstr.strip()
keys = set(al2in.keys())

while len(keys) :
	al = keys.pop()
	iset = set.intersection(*al2in[al])
	if len(iset) == 1:
		print("found one",al,iset)
		item = iset.pop()
		for other in al2in:
			for i in range(len(al2in[other])):
				if item in al2in[other][i]:
					al2in[other][i].remove(item)
	else:
		keys.add(al)

for al in al2in:
	for item in al2in[al]:
		remain = remain.union(item)

print("====")
print(remain)	
#print(allstr)
allwords = allstr.split(' ')
for item in remain:
	for i in range(len(allwords)):
		if item == allwords[i]:
			ct += 1
print(ct)
