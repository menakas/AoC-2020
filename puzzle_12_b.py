import sys 


def turn_right(num):
   global wayx
   global wayy
   tmp = 0
   while num:
       tmp = wayx
       wayx = wayy
       wayy = -tmp
       num -=1
    
def turn_left(num):
   global wayx
   global wayy
   tmp = 0
   while num:
       tmp = wayy
       wayy = wayx
       wayx = -tmp
       num -=1

    
def move(inst):
   global x
   global y
   global wayx
   global wayy
   global dirn
   print inst
   if inst[0:1] == 'F':
       x += (int(inst[1:]) * wayx)
       y += (int(inst[1:]) * wayy)
   if inst[0:1] == 'N':
       wayx -= int(inst[1:]) 
   if inst[0:1] == 'S':
       wayx += int(inst[1:])
   if inst[0:1] == 'W':
       wayy -= int(inst[1:])
   if inst[0:1] == 'E':
       wayy += int(inst[1:])
   if inst[0:1] == 'R':
       turn_right( int(inst[1:])/90)
   if inst[0:1] == 'L':
       turn_left( int(inst[1:])/90)
   print x,y,wayx,wayy,"==="
 
x = 0
y = 0
wayx = -1 
wayy = 10 

for line in sys.stdin:
    line = line.strip()
    move(line)

print abs(x) + abs(y)
