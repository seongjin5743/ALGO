import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

visited = [False] * (n + 1)
parent = [0] * (n + 1)

queue = deque([n])
visited[n] = True

while queue:
    x = queue.popleft()
    
    if x == 1:
        break

    for nx in (x // 3 if x % 3 == 0 else 0, x // 2 if x % 2 == 0 else 0, x - 1):
        if nx > 0 and not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            queue.append(nx)

path = []
cur = 1
while cur:
    path.append(cur)
    cur = parent[cur]

print(len(path) - 1)
print(*path[::-1])