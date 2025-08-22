import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        x = queue.popleft()

        for num in graph[x]:
            if not visited[num]:
                visited[num] = True
                queue.append(num)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1
print(count)