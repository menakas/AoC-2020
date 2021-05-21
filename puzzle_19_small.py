import sys 
import re 
import copy 
from collections import deque


ruleflag = 1
mesg = []
nterms = {}
terms = {}
E = set()
total = 0
CE = set()
def replace_compress():
	for item in E:
		lst = item.split(' ')
		for i in range(len(lst)):
			lst[i] = terms[lst[i]]
		CE.add("".join(lst))
	
def all_done():
	for item in E:
		lst = item.split(' ')
		if not all(trm in terms for trm in lst):
			return item
	return 0


def generate():
	global E
	item = all_done()
	while item:
		E.remove(item)
		print(" ingenerate",len(E))
		lst = list(item.split(' '))
		for i in range(len(lst)):
			if lst[i] in terms:
				continue
			for poss in nterms[lst[i]]:
				E.add((' '.join(lst[0:i])+' ' +poss+' ' + ' '.join(lst[i+1:])).strip())
		item = all_done()
		

		
 


for line in sys.stdin:
	print(line)
	line = line.strip()
	line = re.sub('"','',line)
	if line == '':
		ruleflag = 0
		continue
	if ruleflag :
		(lhs,rhs) = line.split(': ')
		if rhs in 'ab':
			terms[lhs] = rhs
		else:
			nterms[lhs] = []
			rules = rhs.split(' | ')
			for rl in rules:
				nterms[lhs].append(rl)
	else:
		mesg.append(line)


print(nterms,"===")
print(terms)
print(mesg)

E.add('0')
generate()
replace_compress()
print(CE)
for msg in mesg:
	print(msg,"ryinga")
	if msg in CE:
		total +=1

print(total)	
 
