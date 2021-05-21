import sys 
 
acc = 0 

lines = []
visited = {}
for line in sys.stdin:
    line = int(line.strip())
    lines.append(line)

#Use 5 instead of 25 for smple
for index in range(25,len(lines)-1):
    found = 0
    for j in range(index -25,index -1):
        if found == 1:
            break
        for k in range(j+1,index):
            #print "Trying...", lines[j],lines[k],lines[index]
            if lines[j] + lines[k] == lines[index]:
                found = 1
                break
    if found == 0:
        print "Found",lines[index] 
        exit()
