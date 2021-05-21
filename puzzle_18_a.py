import sys 
import re 


def do_arith(one,op,two):
   print(one,op,two)
   if op =='*':
      return one * two
   if op =='/':
      return one / two
   if op =='-':
      return one - two
   if op =='+':
      return one + two

def is_operator(op):
   if len(op) > 1:
       return 0
   if op in "+-*/":
       return 1

def evaluate():
   global index
   print("Starting",index)
   stack = []
   while index < ln:
       print("STack: ",stack)
       if expns[index].isnumeric():
           if len(stack) > 1:
               operator = stack.pop()
               first = stack.pop()
               stack.append(do_arith(first,operator,int(expns[index])))
           else:
               stack.append(int(expns[index]))
       elif is_operator(expns[index]):
           stack.append(expns[index])
       elif expns[index] == '(':
           index +=1
           val = evaluate()
           if len(stack) > 1:
               operator = stack.pop()
               first = stack.pop()
               stack.append(do_arith(first,operator,val))
           else:
               stack.append(val)
       elif expns[index] == ')':
           return stack[0]
       index +=1
   return stack[0]


sum = 0
ln = 0
index = 0
for line in sys.stdin:
    print(line)
    line = line.strip()
    line = line.replace('(','( ')
    line = line.replace(')',' )')
    expns = line.split(' ')
    ln = len(expns)
    index = 0
    sum += evaluate()
 
print(sum)
