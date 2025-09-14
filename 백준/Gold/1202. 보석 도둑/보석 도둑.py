import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jewels = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))

for _ in range(k):
    bags.append(int(input()))

jewels.sort(key= lambda x: x[0])

bags.sort()
value = []
j = 0
answer = 0

for bag in bags:
    while j < n and jewels[j][0] <= bag:
        heapq.heappush(value, -jewels[j][1])
        j += 1
    if value:
        answer += -heapq.heappop(value)

print(answer)