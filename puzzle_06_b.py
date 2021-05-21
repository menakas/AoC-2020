import sys 
import re 
 
valid = 0 


groups = []
 
group= {}

ct = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
      filtered_group = {k for (k,v) in group.items() if ct == v}
      print filtered_group, len(filtered_group)
      groups.append(filtered_group)
      ct=0
      group = {}
      filtered_group = {}
      continue
    ct +=1
    for asc in range(97,123):
      letter = str(chr(asc))
      if len(re.findall(letter,line)) == 1 :
         if letter in group.keys():
           group[letter] += 1
         else:
           group[letter] = 1
      
filtered_group = {k for (k,v) in group.items() if ct == v}
print filtered_group, len(filtered_group)
groups.append(filtered_group)

total = 0

for group in groups:
  total += len(group)

print total 
