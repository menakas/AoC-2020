import sys 
 
def try_this():
  index = 0
  acc = 0
  visited = {}
  while index < len(lines):
      (instruction, arg) = lines[index].split(' ')
      #print instruction, arg
      if visited.has_key(index):
          print "Not this",acc
          return
      visited[index] = 1
      if instruction == 'nop':
          index +=1
      if instruction == 'acc':
          acc += int(arg)
          index +=1
      if instruction == 'jmp':
          index += int(arg)
          
  if index == len(lines):
      print "Found :",acc

lines = []
for line in sys.stdin:
    line = line.strip()
    lines.append(line)

for i in range(len(lines)):
    copy = lines[i]
    (instruction, arg) = lines[i].split(' ')
    print lines[i]
    if instruction == 'nop':
       lines[i] = 'jmp '+ arg
       print i, " changing..............", lines[i], "="
       try_this()
       lines[i]= copy
    if instruction == 'jmp':
       lines[i] = 'nop '+ arg
       print i, " changing.........", lines[i], "="
       try_this()
       lines[i]= copy

