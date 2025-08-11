n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))
num = {}

for n in nums:
    if n in num:
        num[n] += 1
    else:
        num[n] = 1

nums.sort(key= lambda x: (-num[x], x))

print(nums[0])