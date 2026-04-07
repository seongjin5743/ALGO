import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort()

answer = []
for i in range(n):
    answer.append(nums[i] + nums[-(i + 1)])
print(min(answer))