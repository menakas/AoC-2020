import sys
import copy
import pprint


al2in = {}
remain = set()
done = {}
for line in sys.stdin:
	line = line.strip()
	line = line.rstrip(")")
	(instr,alstr) = line.split(" (contains ")
	allist = alstr.split(", ")
	for al in allist:
		if al not in al2in:
			al2in[al] = []
		al2in[al].append(set(instr.split(' ')))

keys = set(al2in.keys())

while len(keys) :
	al = keys.pop()
	iset = set.intersection(*al2in[al])
	if len(iset) == 1:
		print("found one",al,iset)
		item = iset.pop()
		done[al] = item
		for other in al2in:
			for i in range(len(al2in[other])):
				if item in al2in[other][i]:
					al2in[other][i].remove(item)

	else:
		keys.add(al)

print("====")
for al in al2in:
	for item in al2in[al]:
		remain = remain.union(item)

done_keys = sorted(done.keys())

allstr = ''
for i in range(len(done_keys)):
	allstr += ',' + done[done_keys[i]]

allstr = allstr.lstrip(',')
print(allstr)
