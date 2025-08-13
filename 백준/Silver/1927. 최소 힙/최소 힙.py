import heapq
import sys

input = sys.stdin.readline

n = int(input())

nums = []
answer = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if nums:
            answer.append(heapq.heappop(nums))
        else:
            answer.append(0)
    else:
        heapq.heappush(nums, x)

for an in answer:
    print(an)