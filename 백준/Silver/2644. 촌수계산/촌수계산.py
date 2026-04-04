import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

p1, p2 = map(int, input().split())

people = [[] for _ in range(n + 1)]

num = int(input())

for _ in range(num):
    x, y = map(int, input().split())
    people[x].append(y)
    people[y].append(x)

visited = [False] * (n + 1)

queue = deque()
queue.append((p1, 0))
visited[p1] = True

answer = 0

while queue:
    x, cnt = queue.popleft()

    if x == p2:
        answer = cnt
        break

    for i in people[x]:
        if not visited[i]:
            visited[i] = True
            queue.append((i, cnt + 1))

if answer == 0:
    print(-1)
else:
    print(answer)