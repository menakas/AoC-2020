import sys 

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

ones = 0
threes = 1
for i in range(len(jolts)-1):
    if jolts[i+1] - jolts[i] == 3:
         threes +=1
    if jolts[i+1] - jolts[i] == 1:
         ones +=1

print ones,threes, ones * threes
