import sys 


def turn_left(num):
   global dirn
   dirn -= num
   if dirn < 1:
       dirn  += 4
    
def turn_right(num):
   global dirn
   dirn += num
   if dirn > 4:
       dirn  -= 4
    
def move(inst):
   global x
   global y
   global dirn
   print inst
   if inst[0:1] == 'F':
       if dirn == 1:
           y += int(inst[1:])
       if dirn == 3:
           y -= int(inst[1:])
       if dirn == 2:
           x += int(inst[1:])
       if dirn == 4:
           x -= int(inst[1:])
   if inst[0:1] == 'N':
       x -= int(inst[1:])
   if inst[0:1] == 'S':
       x += int(inst[1:])
   if inst[0:1] == 'W':
       y -= int(inst[1:])
   if inst[0:1] == 'E':
       y += int(inst[1:])
   if inst[0:1] == 'R':
       turn_right( int(inst[1:])/90)
   if inst[0:1] == 'L':
       turn_left( int(inst[1:])/90)
   print x,y,dirn,"==="
 
dirn = 1
x = 0
y = 0

for line in sys.stdin:
    line = line.strip()
    move(line)

print abs(x) + abs(y)
