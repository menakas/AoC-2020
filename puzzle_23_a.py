import sys

#inpt = '389125467'
inpt = '792845136'

cups = list(inpt)

mx = 9

def pick3(crt):
	three = []
	if crt == len(cups) -1:
		three.extend(cups[0:3])
		del cups[0:3]
	elif crt == len(cups) -2:
		three.extend(cups[-1:])
		three.extend(cups[0:2])
		del cups[-1]
		del cups[0:2]
	elif crt == len(cups) -3:
		three.extend(cups[-2:])
		three.extend(cups[0:1])
		del cups[-2:]
		del cups[0]
	else:
		three.extend( cups[crt+1:crt+4])
		del cups[crt+1: crt+4]
	print("in pick", cups,three)
	return three

def get_destn(crt,three):
	print(three,crt)
	label = int(cups[crt])
	dest = label -1
	if dest == 0:
		dest = mx
	while str(dest) in three:
		dest -=1
		if dest == 0:
			dest = mx
	destind = cups.index(str(dest))
	print(cups,destind,dest)
	return (destind,str(dest))


current = 0

moves = 100
mcount = 0
while mcount < moves:
	print("\n===",current,cups)
	clabel = cups[current]
	three = []
	three.extend(pick3(current))
	current = cups.index(clabel)
	(destind,destn) = get_destn(current,three)
	del cups[destind]
	cups.insert(destind,destn)
	cups[destind+1:destind+1] = three
	if destind < current:
		current +=3
	current +=1
	if current >= len(cups):
		current = 0	
	mcount +=1

print("****",cups)

start = cups.index('1')

lst = cups[start+1:]+cups[0:start]
print(''.join(lst))
