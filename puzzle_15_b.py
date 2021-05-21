import sys 

nums = []

#mx = 2020
mx = 30000000

for line in sys.stdin:
    print line
    line = line.strip()
    nums = line.split(',')

lastindex = {}
firstindex = {}
for i in range(len(nums)):
    nums[i] = int(nums[i])
    firstindex[nums[i]] = i


print nums


start = len(nums)
last = nums[len(nums)-1]
for i in range(start,mx): 
    print i
    if nums[i-1] in lastindex and nums[i-1] in firstindex:
        nums.append(lastindex[nums[i-1]] - firstindex[nums[i-1]])
    elif nums[i-1] in firstindex:
        nums.append(0)

    if nums[i] in lastindex  and nums[i] in firstindex:
        firstindex[nums[i]] = lastindex[nums[i]]
        lastindex[nums[i]] = i
    elif nums[i] in firstindex:
        lastindex[nums[i]] = i
    else:
        firstindex[nums[i]] = i
        
#print nums
print nums[2019]
print nums[29999999]
