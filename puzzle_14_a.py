import sys 


matrix = []
mask = ''
total = 0
def decimalToBinary(n):  
    return bin(n).replace("0b", "")  

def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return  decimal

def get_value(ind, val):
    global mask
    valstr = []
    valstr = [char for char in (str(decimalToBinary(val)).rjust(len(mask),'0'))]
    print valstr, "---"
    for j in range(len(mask)):
        if mask[j] != 'X':
            valstr[j] = mask[j]
    sm  = ''.join(map(str, valstr)) 
    print int(sm),"===="
    
    return binaryToDecimal(int(sm))
           
for i in range(mx):
    matrix.append(0)
for line in sys.stdin:
    print line
    line = line.strip()
    (inst,value) = line.split(' = ')
    if inst == 'mask':
        mask = value
    elif inst[0:3] == 'mem':
        index = inst[4:]
        index = int(index[:-1])
        matrix[index] = get_value(index,int(value)) 

for i in range(mx):
    total += matrix[i]

print total
