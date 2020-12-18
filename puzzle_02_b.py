import sys 
 
valid = 0 
  
for line in sys.stdin: 
    line = line.strip()
    words = line.split()
    (first,second) = words[0].split('-')
    words[1] = words[1][:-1]
    cnt = words[2].count(words[1])
    if int(words[2][int(first)-1] == words[1]) + int(words[2][int(second)-1] == words[1] ) == 1:
      valid += 1
  
print(valid)
