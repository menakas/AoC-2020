import sys 

rules = []
rulenames = []
all_rules = {}
near_tickets = []

results = []
myticket = 0
neartickets = 0

irule = 0
for line in sys.stdin:
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
        rulelists = rrule.split(' or ')
        rules.append({})
        for item in rulelists:
            (start,end) = item.split('-')
            for j in range(int(start),int(end)+1):
            	all_rules[j] = 1
                rules[irule][j] = 1
        irule+=1
    elif not neartickets:
       my_ticket = line.split(',')
    else:
       near_list = line.split(',')
       near_tickets.append(near_list) 

print all_rules.keys()

error_rate = 0
new_near_tickets = []
for i in range(len(near_tickets)):
    vals = near_tickets[i]
    valid = 1
    for val in vals:
        if int(val) not in all_rules.keys():
            valid = 0
    if valid:
        new_near_tickets.append(near_tickets[i])
            
new_near_tickets.append(my_ticket)
for i in range(len(rules)):
    results.append([])
    for pos in range(len(new_near_tickets[0])):
        valid = 1
        for j in range(len(new_near_tickets)):
            if int(new_near_tickets[j][pos]) not in rules[i].keys():
                valid = 0
        if valid:
            results[i].append(pos)

lresults={}
for i in range(len(results)):
    results[i].append(rulenames[i])
    lresults[len(results[i])-1] = results[i]


ln = len(lresults)

print lresults
done = {}
for i in range(1,ln+1):
    llist = lresults[i] 
    print llist
    for item in done.values():
       llist.remove(item)
    done[llist[-1]] =  llist[0]


print done.keys()
print my_ticket
product = 1
for item in done.keys():
    print item[0:9],done[item],my_ticket[done[item]]
    if item[0:9] == 'departure':
         product *= int(my_ticket[done[item]])
         print "product........", product


print product
