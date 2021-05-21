import sys

def player_has_no_card(pid):
	if len(players[pid]) == 0:
		return 1

def move(gtp,lsp):
	tmp = players[gtp][0]
	del players[gtp][0]
	players[gtp].append(tmp)
	tmp = players[lsp][0]
	del players[lsp][0]
	players[gtp].append(tmp)

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
	
while not player_has_no_card(0) and not player_has_no_card(1):
	if players[0][0] > players[1][0]:
		move(0,1)
	else:
		move(1,0)

print(players)
if player_has_no_card(0):
	winner = 1
else:
	winner = 0

ln = len(players[winner])

val = 0
for i in range(ln):
	val += (players[winner][ln-1-i] * (i+1))
print(val)
	
