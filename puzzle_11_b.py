import sys 

seats = []

i = 0
for line in sys.stdin:
    line = line.strip()
    seats.append([])
    seats[i] = list(line)
    i+=1

print seats


def count_visible_occupied(i,j):
    count = 0
    x = i-1
    while x >= 0:
        if seats[x][j] == '#':
             count +=1
             break
        if seats[x][j] == 'L':
             break
        x -=1

    x = i+1
    while x < len(seats):
        if seats[x][j] == '#':
             count +=1
             break
        if seats[x][j] == 'L':
             break
        x +=1

    y = j-1
    while y >= 0:
        if seats[i][y] == '#':
             count +=1
             break
        if seats[i][y] == 'L':
             break
        y -=1

    y = j+1
    while y < len(seats[i]):
        if seats[i][y] == '#':
             count +=1
             break
        if seats[i][y] == 'L':
             break
        y  +=1

    x = i-1
    y = j-1
    while x >= 0 and y >= 0:
        if seats[x][y] == '#':
             count +=1
             break
        if seats[x][y] == 'L':
             break
        x -=1
        y -=1

    x = i-1
    y = j+1
    while x >= 0 and y < len(seats[x]):
        if seats[x][y] == '#':
             count +=1
             break
        if seats[x][y] == 'L':
             break
        x -=1
        y +=1

    x = i+1
    y = j-1
    while x < len(seats) and y >= 0:
        if seats[x][y] == '#':
             count +=1
             break
        if seats[x][y] == 'L':
             break
        x +=1
        y -=1

    x = i+1
    y = j+1
    while x < len(seats) and y < len(seats[x]):
        if seats[x][y] == '#':
             count +=1
             break
        if seats[x][y] == 'L':
             break
        x +=1
        y +=1

    return count
         
    
def get_value(i,j):
    if seats[i][j] == '.':
        return '.'
    visible = count_visible_occupied(i,j)
    #print i,j,visible
    if seats[i][j] == 'L' and visible == 0:
        return '#'
    if seats[i][j] == '#' and visible >=5:
        return 'L'
    return seats[i][j]

changed = 1
while changed:
    newseats =[]
    changed = 0
    for i in range(len(seats)):
        newseats.append([])
        for j in range(len(seats[i])):
            newseats[i].append(get_value(i,j))
    #print "======="
    #print newseats
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] != newseats[i][j]:
                 #print "Changed", i, j, seats[i][j], newseats[i][j]
                 changed = 1    
    seats = []
    for i in range(len(newseats)):
        seats.append([])
        for j in range(len(newseats[i])):
            seats[i].append(newseats[i][j])

Total = 0
for i in range(len(seats)):
    for j in range(len(seats[i])):
        if seats[i][j] == '#':
            Total +=1
    
print Total 
