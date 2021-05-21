import sys 
 
acc = 0 

lines = []
visited = {}
for line in sys.stdin:
    line = line.strip()
    lines.append(line)

index = 0
while index < len(lines):
    (instruction, arg) = lines[index].split(' ')
    print instruction, arg
    if visited.has_key(index):
        print acc
        exit()
    visited[index] = 1
    if instruction == 'nop':
        index +=1
    if instruction == 'acc':
        acc += int(arg)
        index +=1
    if instruction == 'jmp':
        index += int(arg)
        
    print acc

