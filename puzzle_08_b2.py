import sys
import re

lines = []

for line in sys.stdin:
    line = line.rstrip()
    lines.append(line)

print lines

def try_this():
    acc = 0
    visited = {}
    j = 0
    while j < len(lines):
        (instruction,arg) = lines[j].split(' ')
        if visited.has_key(str(j)):
            print "Not this",acc
            return 
        visited[str(j)] = 1
        if instruction == 'nop':
            j +=1
        if instruction == 'jmp':
            j += int(arg) 
        if instruction == 'acc':
            acc += int(arg) 
            j +=1
    if j == len(lines):
        print "Found", acc
        exit()



for i in range(len(lines)):
    cpy = lines[i]
    (instruction,arg) = lines[i].split(' ')
    if instruction == 'nop': 
        lines[i] = 'jmp '+ arg
        try_this()
        lines[i] = cpy
    if instruction == 'jmp': 
        lines[i] = 'nop '+ arg
        try_this()
        lines[i] = cpy
