import sys 
 
acc = 0 

lines = []
visited = {}
for line in sys.stdin:
    line = int(line.strip())
    lines.append(line)

invalid = 2089807806
ind = lines.index(invalid)
print ind

#Use 5 instead of 25 for smple
for i in range(ind-1):
    found = 0
    mn = lines[i]
    mx = lines[i]
    total = lines[i]
    print "Trying", i,lines[i]
    for j in range(i+1,ind ):
            total += lines[j]
            if lines[j] < mn:
                mn = lines[j]
            if lines[j] > mx:
                mx = lines[j]
            if total == lines[ind]:
                found = 1
                print "Found",i,j,lines[i],lines[j],total,lines[ind] , mn+mx
                break
