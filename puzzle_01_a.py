import sys

nums = []
for line in sys.stdin:
    line = line.strip()
    nums.append(int(line))

for i in range(0,len(nums)-1):
  for j in range(i+1,len(nums)):
    if (nums[i]  +  nums[j]) == 2020:
      print(nums[i],nums[j],nums[i]*nums[j])

