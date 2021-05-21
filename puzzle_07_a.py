import sys 
from collections import deque

target = 'shinygold'
E = {}

def compress( text ):
    text = text.strip()
    words = text.split(' ')
    out = ''
    for word in words:
        while any([word.startswith(d) for d in '0123456789']):
            word = word[1:]
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
        if bag not in E:
             E[bag] = []
        print(container,bag)
        E[bag].append(container)

SEEN = set()
Q = deque([target])
while Q:
    print Q
    x = Q.popleft()
    print(x)
    if x in SEEN:
        continue
    SEEN.add(x)
    print "Seen", SEEN
    for y in E.get(x,[]):
          Q.append(y)

       
print(len(SEEN)-1)
 
