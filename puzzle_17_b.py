import sys 
import pprint
import copy

def get_neighbours(w,x,y,z,ln):

    #print(x,y,z,ln)
    neighbours = set()
    for h in range(ln):
        if h+1 ==w or h==w or h-1 == w:
            for i in range(ln):
                if i+1 ==x or i==x or i-1 == x:
                    for j in range(ln):
                        if j+1 ==y or j==y or j-1 == y:
                            for k in range(ln):
                                if k+1 ==z or k==z or k-1 == z:
                                    #print("Adding",x,y,z)
                                    if not ( h==w and i==x and j == y and k==z): 
                                        neighbours.add((h,i,j,k))
    #print(neighbours)
    return neighbours

def get_active_neighbours_count(w,x,y,z,ln):
    neighbours = get_neighbours(w,x,y,z,ln)
    #print(w,x,y,z,"NNEIGH : ",neighbours)
    ct = 0
    for neighbour in neighbours:
        if matrix[neighbour[0]][neighbour[1]][neighbour[2]][neighbour[3]] == '#':
            #print(neighbour,"is the ACTIVE nei")
            ct +=1  
    #print(ct)
    return ct
    
def is_active(w,x,y,z):
    if matrix[w][x][y][z] == '#':
        return 1
    else:
        return 0

def copy_new_matrix():
    for h in range(ln):
        for i in range(ln):
             for j in range(ln):
                 for k in range(ln):
                     matrix[h][i][j][k] = new_matrix[h][i][j][k]


matrix = []
new_matrix = []
ln = 0

trs = 6
first = 0
firstln = 0
for line in sys.stdin:
    line = line.strip()
    if not first:
        firstln = len(line)
        ln = firstln + (trs*2)
        matrix = [[[['.' for k in range(ln)] for j in range(ln)] for i in range(ln)] for h in range(ln)]
        new_matrix = [[[['.' for k in range(ln)] for j in range(ln)] for i in range(ln)] for h in range(ln)]
    tmp_list = list(line)
    for j in range(firstln):
        matrix[trs][trs][trs+first][trs+j] = tmp_list[j]
    first +=1


print("length is",ln)
pprint.pprint(matrix)


print("\n\n\n")
first = 1
for rnd in range(0,trs):
    print("\n","ROUND ", rnd, ":\n")
    start = 0
    stop = ln
    for h in range(start,stop):
        for i in range(start,stop):
            for j in range(start,stop):
                for k in range(start,stop):
                    active_neighbours_count = get_active_neighbours_count(h,i,j,k,ln) 
                    #print(h,i,j,k,matrix[i][j][k], active_neighbours_count)
                    if is_active(h,i,j,k) and ( active_neighbours_count < 2 or active_neighbours_count > 3 ):
                        print("Deactivating",h,i,j,k)
                        new_matrix[h][i][j][k] = '.'                
                    elif ( not is_active(h,i,j,k) ) and active_neighbours_count == 3 :
                        print("Activating",h,i,j,k)
                        new_matrix[h][i][j][k] = '#'                
                    else:
                        new_matrix[h][i][j][k] = matrix[h][i][j][k]
    pprint.pprint(new_matrix)
    #pprint.pprint([{num: value} for num, value in enumerate(new_matrix)], width=20)
    if first:
       first = 0
       rnd = -1 
    copy_new_matrix()
    #pprint.pprint(matrix)
    print("===========\n\n")

active = 0
for h in range(ln):
    for i in range(ln):
        for j in range(ln):
            for k in range(ln):
                if matrix[h][i][j][k] == '#':
                    active+=1
print(active)
