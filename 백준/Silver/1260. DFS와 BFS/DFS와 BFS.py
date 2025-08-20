from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for edges in graph:
    edges.sort()

dfs_list = []
bfs_list = []

def dfs(x, graph, visited):
    visited[x] = True
    dfs_list.append(x)
    for i in graph[x]:
        if not visited[i]:
            dfs(i, graph, visited)

def bfs(x, graph, visited):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        v = queue.popleft()
        bfs_list.append(v)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
visited = [False] * (n + 1)
dfs(v, graph, visited)
visited = [False] * (n + 1)
bfs(v, graph, visited)

print(*dfs_list)
print(*bfs_list)