import sys 
import re 
import copy 
# CYK algorithm

for line in sys.stdin:
	#print(line)
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


#print(nterms,"===")
#print(terms)
#print(mesg)

for msg in mesg:
	print(msg,"MESG")
	n = len(msg)
	r = len(nterms)
	P = [[[ False for k in range(r)] for j in range(n)] for i in range(n)]
	for i in range(n):
		P[1][i][
	ln = len(stack)
	#print(stack,"STARTINNG")
	if parse('0',0,0):
		print("Parsed")
		if ind != ln:
			print("BUT", ind)
		total+=1
		print("MAtch")

print(total)	
