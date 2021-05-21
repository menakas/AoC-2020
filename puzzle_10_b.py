import sys 
from collections import deque

jolts = [0]

def insert_jolt(jolt):
    if len(jolts) == 1:
        jolts.insert(1,jolt)
        return
    for i in range(1,len(jolts)):
        if jolts[i] > jolt:
            jolts.insert(i,jolt)
            return
    jolts.insert(len(jolts),jolt) 

for line in sys.stdin:
    line = line.strip()
    insert_jolt(int(line))

print jolts

E = {}
for i in range(len(jolts) -1):
    for j in range(i+1,i+4):
        if j >= len(jolts):
            break
        if jolts[j] - jolts[i] <=3:
           fr  = jolts[i]
           if fr not in E:
               E[fr] = []
           to  = jolts[j]
           E[fr].append(to)
  
numarrs = {}
def num_arrs(x):
   num = 0
   if x not in E:
      return 1
   for item in E.get(x,[]):
      if numarrs.has_key(item):
          num += numarrs[item]
      else:
          num += num_arrs(item)
   numarrs[x] = num
   return num

print num_arrs(0)       
