import sys 
 
valid = 0 


groups = []
 
group= {}
for line in sys.stdin:
    line = line.strip()
    if not line:
      groups.append(group)
      group = {}
      continue
    for element in range(0, len(line)):
      group[line[element]] = 1
    print group
groups.append(group)

total = 0

for group in groups:
  total += len(group)

print total 
