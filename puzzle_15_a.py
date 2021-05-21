import sys 


nums = []

lastindex = {}

mx = 30000000

for line in sys.stdin:
    print line
    line = line.strip()
    nums = line.split(',')

for i in range(len(nums)):
    #lastindex[str(nums[i])] = i
    nums[i] = int(nums[i])


print nums

start = len(nums)
last = nums[len(nums)-1]
for i in range(start,mx): 
    print i
    #print nums
    indexes = [index for index in range(len(nums)) if nums[index] == nums[i-1] ]
    if len(indexes) > 1:
        nums.append(indexes[len(indexes)-1] - indexes[len(indexes)-2])
    else:
        nums.append(0)
    #print indexes

print nums
print nums[2019]
print nums[29999999]
