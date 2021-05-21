import sys 
from collections import deque

target = 'shinygold'
p1 = 0
p2 = 0
E = {}

def compress( text ):
    text = text.strip()
    words = text.split(' ')
    out = ''
    for word in words:
        if 'bag' in word:
            continue
        out += word
    return out


for line in sys.stdin:
    line = line.strip()
    (container,contents) = line.split(' contain ')
    container = compress(container)
    bags = contents.split(',')
    for bag in bags:
        bag = compress(bag)
        if bag == 'noother':
            break
        if container not in E:
             E[container] = []
        print(container,bag)
        E[container].append((int(bag[0:1]),bag[1:]))

print E

def num_bags(bag):
    num = 1
    for (n,x) in E.get(bag,[]):
         print bag,n,x,num
         num += (n * num_bags(x)) 
         print bag,n,x,num, "=="

    return num
       
print(num_bags(target)-1)
 
