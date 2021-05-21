import sys
import pprint
import copy

def player_has_no_card(cards):
	if len(cards) == 0:
		return 1

def move(cards1,cards2):
	tmp = cards1[0]
	del cards1[0]
	cards1.append(tmp)
	tmp = cards2[0]
	del cards2[0]
	cards1.append(tmp)
	return cards1

def get_str(lst):
	print(lst)
	st = ''
	for i in range(len(lst)):
		st = st+ str(lst[i]) + ":"
	print(st)
	return st

def recurse(cards1,cards2):
	print("Recursing")
	all_cards1 = set()
	all_cards2 = set()
	
		
	while not player_has_no_card(cards1) and not player_has_no_card(cards2):
		if get_str(cards1) in all_cards1 or get_str(cards2)	in all_cards2:
			return (0,cards1)
		all_cards1.add(get_str(cards1))
		all_cards2.add(get_str(cards2))
		print(cards1)
		print(cards2)
		if cards1[0] <= len(cards1)-1 and cards2[0] <= len(cards2)-1:
			(winner,tmp) = recurse(cards1[1:cards1[0]+1].copy(),cards2[1:cards2[0]+1].copy())
			if winner == 0:
				cards1 = move(cards1.copy(),cards2.copy())
				del cards2[0]
			else:
				cards2 = move(cards2.copy(),cards1.copy())
				del cards1[0]
		elif cards1[0] > cards2[0]:
			cards1 = move(cards1.copy(),cards2.copy())
			del cards2[0]
		else:
			cards2 = move(cards2.copy(),cards1.copy())
			del cards1[0]
	
	if not player_has_no_card(cards1):
		return (0,cards1)
	else:
		return (1,cards2)
	
players = []
player = -1
for line in sys.stdin:
	line = line.strip()
	if not line:
		continue	
	if 'Player' in line:
		player+=1
		players.append([])
	else:
		players[player].append(int(line))
	
(winner,cards) = recurse(players[0],players[1])
ln = len(cards)

val = 0
for i in range(ln):
	val += (cards[ln-1-i] * (i+1))
print(val)
	
