import sys 
import re 
 
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
  for item in keyList:
    if item in record.keys():
      #print item
      if item == 'byr' and int(record[item]) >= 1920 and int(record[item]) <=2002:
        ct+=1
      if item == 'iyr' and int(record[item]) >= 2010 and int(record[item]) <=2020:
        ct+=1
      if item == 'eyr' and int(record[item]) >= 2020 and int(record[item]) <=2030:
        ct+=1
      if item == 'hgt':
        if record[item][3:] == 'cm' and int(record[item][0:3]) >= 150 and int(record[item][0:3]) <=193:
          ct+=1
        if record[item][2:] == 'in' and int(record[item][0:2]) >= 59 and int(record[item][0:2]) <=76:
          ct+=1
      if item == 'hcl' and len(re.findall("#[a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9]",record[item]))  == 1:
        ct+=1
      if item == 'ecl' and record[item] in [ 'amb','blu','brn','gry','grn','hzl','oth' ]:
        ct+=1
      if item == 'pid' and len(re.findall("^[0-9]{9}$",record[item])) == 1:
        ct+=1

  if ct == 7:
    #print(record)
    valid+=1 
 

print ( valid )
