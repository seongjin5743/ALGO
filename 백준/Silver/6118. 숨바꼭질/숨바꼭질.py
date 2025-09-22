from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [int(1e6)] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = deque()
    queue.append((x, 0))
    visited[x] = True

    while queue:
        x, cnt = queue.popleft()
        distance[x] = min(distance[x], cnt)

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, cnt + 1))

bfs(1)
answer = 0

for dis in distance:
    if dis != 1000000:
        answer = max(answer, dis)

print(distance.index(answer), answer, distance.count(answer))