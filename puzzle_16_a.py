import sys 

rules = []
rulenames = []
all_rules = {}
near_tickets = []

myticket = 0
neartickets = 0

irule = 0
for line in sys.stdin:
    print line
    line = line.strip()
    if line == '':
       continue
    elif line == 'your ticket:':
       myticket = 1
    elif line == 'nearby tickets:':
       neartickets = 1
    elif not myticket:
        (rname,rrule) = line.split(': ')
        rulenames.append(rname)
        rules.append(rrule)
        rulelists = rrule.split(' or ')
        for item in rulelists:
            (start,end) = item.split('-')
            for j in range(int(start),int(end)+1):
            	all_rules[j] = 1
    elif not neartickets:
       my_ticket = line
    else:
       near_list = line.split(',')
       for item in near_list:
           near_tickets.append(item) 


print all_rules.keys()
print near_tickets

error_rate = 0
for i in range(len(near_tickets)):
    vals = near_tickets[i].split(',')
    for val in vals:
        print "val", val
        if int(val) not in all_rules.keys():
            error_rate +=int(val)


print error_rate
