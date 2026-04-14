import sys
input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]

nums.sort()

arr = set()

for x in nums:
    for y in nums:
        arr.add(x + y)

for k in range(n - 1, -1, -1):
    for z in range(k + 1):
        if nums[k] - nums[z] in arr:
            print(nums[k])
            exit()