import sys 

mask = ''
total = 0
E = {}

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


def write_bits(ind, addr,val):
    global matrix
    if ind == len(mask):
        print "END writing",val, "to ",binaryToDecimal(int(addr))
        E[binaryToDecimal(int(addr))]  = val
    elif mask[ind] == '1':
        write_bits(ind+1,addr[0:ind]+'1'+addr[ind+1:],val)
    elif mask[ind] == 'X':
        write_bits(ind+1,addr[0:ind]+'0'+addr[ind+1:],val)
        write_bits(ind+1,addr[0:ind]+'1'+addr[ind+1:],val)
    else:
        write_bits(ind+1,addr,val)
        
for line in sys.stdin:
    print line
    line = line.strip()
    (inst,value) = line.split(' = ')
    if inst == 'mask':
        mask = value
    elif inst[0:3] == 'mem':
        index = inst[4:]
        index = int(index[:-1])
        indstr = [char for char in (str(decimalToBinary(index)).rjust(len(mask),'0'))]
        write_bits(0,''.join(map(str,indstr)),int(value))

print E
for item in E:
    print item
    total += E[item]

print total
