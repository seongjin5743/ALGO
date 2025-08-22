from collections import deque

f,s,g,u,d = map(int, input().split())

visited = [False] * (f + 1)

def bfs(start, end):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True
    while queue:
        x, count = queue.popleft()

        if x == end:
            return count

        for i in [u, -d]:
            nx = x + i

            if 0 < nx <= f and not visited[nx]:
                queue.append((nx, count + 1))
                visited[nx] = True
    return 'use the stairs'

print(bfs(s, g))