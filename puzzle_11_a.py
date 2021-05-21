import sys 

seats = []

i = 0
for line in sys.stdin:
    line = line.strip()
    seats.append([])
    print line
    seats[i] = list(line)
    i+=1

print seats


def count_adjacent_occupied(i,j):
    count = 0
    print i,j
    if  i == 0:
        if j== 0:
#             print "both", seats[i][j+1],seats[i+1][j+1],seats[i+1][j]
             if seats[i][j+1] == '#':
                 count +=1 
             if seats[i+1][j+1] == '#':
                 count +=1 
             if seats[i+1][j] == '#':
                 count +=1 
        elif j ==  len(seats[0])-1:
             if seats[i][j-1] == '#':
                 count +=1 
             if seats[i+1][j-1] == '#':
                 count +=1 
             if seats[i+1][j] == '#':
                 count +=1 
        else:
             if seats[i][j+1] == '#':
                 count +=1 
             if seats[i+1][j+1] == '#':
                 count +=1 
             if seats[i+1][j] == '#':
                 count +=1 
             if seats[i][j-1] == '#':
                 count +=1 
             if seats[i+1][j-1] == '#':
                 count +=1 
    elif i == len(seats)-1:
        if j== 0:
             if seats[i][j+1] == '#':
                 count +=1 
             if seats[i-1][j+1] == '#':
                 count +=1 
             if seats[i-1][j] == '#':
                 count +=1 
        elif j ==  len(seats[0])-1:
             if seats[i][j-1] == '#':
                 count +=1 
             if seats[i-1][j-1] == '#':
                 count +=1 
             if seats[i-1][j] == '#':
                 count +=1 
        else:
             if seats[i][j+1] == '#':
                 count +=1 
             if seats[i-1][j-1] == '#':
                 count +=1 
             if seats[i-1][j] == '#':
                 count +=1 
             if seats[i][j-1] == '#':
                 count +=1 
             if seats[i-1][j+1] == '#':
                 count +=1 
    else:
        if j== 0:
             if seats[i][j+1] == '#':
                 count +=1 
             if seats[i-1][j+1] == '#':
                 count +=1 
             if seats[i+1][j+1] == '#':
                 count +=1 
             if seats[i-1][j] == '#':
                 count +=1 
             if seats[i+1][j] == '#':
                 count +=1 
        elif j ==  len(seats[0])-1:
             if seats[i][j-1] == '#':
                 count +=1 
             if seats[i+1][j-1] == '#':
                 count +=1 
             if seats[i+1][j] == '#':
                 count +=1 
             if seats[i-1][j-1] == '#':
                 count +=1 
             if seats[i-1][j] == '#':
                 count +=1 
        else:
             if seats[i][j-1] == '#':
                 count +=1 
             if seats[i][j+1] == '#':
                 count +=1 
             if seats[i-1][j-1] == '#':
                 count +=1 
             if seats[i-1][j+1] == '#':
                 count +=1 
             if seats[i+1][j-1] == '#':
                 count +=1 
             if seats[i+1][j+1] == '#':
                 count +=1 
             if seats[i-1][j] == '#':
                 count +=1 
             if seats[i+1][j] == '#':
                 count +=1 
    #print "Count", count

    return count
         
    
def get_value(i,j):
    if seats[i][j] == '.':
        return '.'
    adjacent = count_adjacent_occupied(i,j)
    #print i,j,adjacent
    if seats[i][j] == 'L' and adjacent == 0:
        return '#'
    if seats[i][j] == '#' and adjacent >=4:
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
    print "======="
    print newseats
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
