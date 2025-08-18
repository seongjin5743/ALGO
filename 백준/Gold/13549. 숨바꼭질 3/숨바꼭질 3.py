from collections import deque

n, k = map(int, input().split())

INF = 100001
visited = [False] * INF

def bfs(x, target):
    queue = deque()
    queue.append((x, 0))
    visited[x] = True

    while queue:
        x, count = queue.popleft()

        if x == target:
            return count

        nx = x * 2
        if 0 <= nx < INF and not visited[nx]:
            visited[nx] = True
            queue.append((nx, count))

        nx = x - 1
        if 0 <= nx < INF and not visited[nx]:
            visited[nx] = True
            queue.append((nx, count + 1))

        nx = x + 1
        if 0 <= nx < INF and not visited[nx]:
            visited[nx] = True
            queue.append((nx, count + 1))
print(bfs(n, k))