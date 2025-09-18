from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(1, n + 1):
    citys = list(map(int, input().split()))
    for j in range(n):
        if citys[j] == 1:
            graph[i].append(j + 1)

route = list(map(int, input().split()))

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        for nxt in graph[x]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

bfs(route[0])

if all(visited[city] for city in route):
    print("YES")
else:
    print("NO")