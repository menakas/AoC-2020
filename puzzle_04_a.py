import sys 
 
valid = 0 


keyList = ["ecl","pid","eyr","hcl","byr","iyr","hgt"]
records = []
 
record = {}
for line in sys.stdin:
    line = line.strip()
    if not line:
      records.append(record.copy())
      record = {}
      continue
    words = line.split(' ')
    for word in words:
      (key,value) = word.split(':')
      record[key] = value
records.append(record.copy())

for record in records:
  ct = 0
  #print(record)
  for item in keyList:
    if item in record.keys():
      #print item
      ct+=1
  #print ct
  if ct == 7:
    valid+=1 
 

print(valid) 
