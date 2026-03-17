import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

dic = {}

for num in nums:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

n = len(dic)

if n == 3:
    print(100 * max(nums))
elif n == 2:
    for k, v in dic.items():
        if v == 2:
            print(1000 + k * 100)
else:
    print(10000 + nums[0] * 1000)