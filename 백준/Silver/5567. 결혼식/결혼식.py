from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True
    count = 0

    while queue:
        x, depth = queue.popleft()
        if depth == 2:
            continue
        for friend in graph[x]:
            if not visited[friend]:
                visited[friend] = True
                count += 1
                queue.append((friend, depth + 1))
    return count

print(bfs(1))