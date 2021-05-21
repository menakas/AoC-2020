import sys 
import re 
import copy 


ruleflag = 1
mesg = []
nterms = {}
terms = {}
ind = 0
total = 0
ln = 0
	

def parse(rule):
	global stack
	global ind
	if ind >= ln:
		return 0
	print("parse..rule",rule,"index",ind)
	if rule in nterms:
		anyrule = 0
		index = ind
		for rrule in nterms[rule]: #each different possibility
			ind = index
			lst = rrule.split(' ')
			print(lst)
			parsed = 1
			for i in range(len(lst)): #each component of a rule
				if not parse(lst[i]):
					parsed = 0
					break
			if parsed:
				anyrule = ind
		if anyrule:
			ind = anyrule
		return anyrule
	elif rule in terms:	
		token = stack[ind]
		if token == terms[rule]:
			print("Match", token, "index", ind,"\n")
			ind+=1
			return 1
		else:
			print("NNNNOMatch", token, "index", ind,"\n")
			return 0
			

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

for msg in mesg:
	ind = 0
	print(msg,"MESG")
	stack = list(msg)
	ln = len(stack)
	print(stack,"STARTINNG")
	if parse('0') and ind == ln:
		total+=1

print(total)	
