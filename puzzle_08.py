import fileinput
import re
from copy import deepcopy

def run(P, ip, acc):
    words = P[ip]
    if words[0] == 'acc':
        acc += int(words[1])
        ip += 1
    elif words[0] == 'nop':
        ip += 1
    elif words[0] == 'jmp':
        ip += int(words[1])
    return (ip, acc)

P = list([l.split() for l in fileinput.input()])
ip = 0
acc = 0
seen = set()
while True:
    if ip in seen:
        print(acc)
        break
    seen.add(ip)
    ip, acc = run(P, ip, acc) 

for change in range(len(P)):
    Pmod = deepcopy(P)
    if Pmod[change][0] == 'nop':
        Pmod[change][0] = 'jmp'
    elif Pmod[change][0] == 'jmp':
        Pmod[change][0] = 'nop'
    else:
        continue
    t = 0
    ip = 0
    acc = 0
    while 0<=ip<len(Pmod) and t<1000:
        t += 1
        ip, acc = run(Pmod, ip, acc)
    if ip == len(Pmod):
        print(acc)

