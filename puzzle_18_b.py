import sys 
import re 


def do_arith(one,op,two):
   if op =='*':
      return one * two
   if op =='/':
      return one / two
   if op =='-':
      return one - two
   if op =='+':
      return one + two

def map_brackets():
   global bmap
   index = 0
   lastopen = []

   bmap= {}
   while index < len(expns):
       if expns[index] == '(':
           lastopen.append(index)
       if expns[index] == ')':
           key = lastopen.pop()
           bmap[key] = index
       index +=1 

 
def evaluate(start,end):

   print("In evaluate",start,end)
   plus = start 
   while plus < end:
       if expns[plus] == '+':
          #print("INDEX",plus,"PLUS",expns[plus-1],expns[plus],expns[plus+1],"END",end)
          if expns[plus-1].isnumeric() and expns[plus+1].isnumeric():
              expns[plus-1] = str(do_arith(int(expns[plus-1]),'+',int(expns[plus+1])))
              del expns[plus:plus+2] 
              end -=2
              plus -=1
              print(expns)
          if expns[plus].isnumeric() and (plus > 0) and expns[plus-1] == '(' and (plus+1 < len(expns)) and expns[plus+1] == ')':
              print("removing ()()()()()")
              expns[plus-1]= expns[plus]
              del expns[plus:plus+2]
              print(expns)
              end -=2
       plus +=1
        
   oper = start 
   while oper < end:
       if expns[oper] in '-/*':
          if expns[oper-1].isnumeric() and expns[oper+1].isnumeric():
              expns[oper-1] = str(do_arith(int(expns[oper-1]),expns[oper],int(expns[oper+1])))
              del expns[oper:oper+2] 
              end -=2
              print(expns)
              oper -=1
          if expns[oper].isnumeric() and (oper > 0) and expns[oper-1] == '(' and (oper+1 < len(expns)) and expns[oper+1] == ')':
              print("removing ()()()()()")
              expns[oper-1]= expns[oper]
              del expns[oper:oper+2]
              print(expns)
              end -=2
       oper +=1


total = 0
bmap = {}
for line in sys.stdin:
    print(line)
    line = line.strip()
    line = line.replace('(','( ')
    line = line.replace(')',' )')
    expns = line.split(' ')
    print(expns)
    while len(expns) > 1:
       map_brackets()
       keymap = sorted(bmap.keys())
       if len(keymap) == 0:
            break
       start = keymap[-1]
       evaluate(start,bmap[start])
       print("....................................................Round",expns)
    evaluate(0,len(expns))
    total += int(expns[0])
 
print(total)
