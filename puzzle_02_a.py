import sys 
 
valid = 0 
  
for line in sys.stdin: 
    line = line.strip()
    words = line.split()
    #print(words)
    (minct,maxct) = words[0].split('-')
    words[1] = words[1][:-1]
    cnt = words[2].count(words[1])
    #print(cnt)
    if cnt >= int(minct) and cnt <= int(maxct):
      valid += 1
  
print(valid)
