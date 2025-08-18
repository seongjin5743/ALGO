from collections import deque

n, k = map(int, input().split())

visited = [False] * (100001)

def bfs(x, target):
    queue = deque()
    queue.append((x, 0))
    visited[x] = True

    while queue:
        x, count = queue.popleft()

        if x == target:
            return count
        
        for nx in (x * 2, x + 1, x - 1):
            if 0 <= nx < 100001 and not visited[nx]:
                queue.append((nx, count + 1))
                visited[nx] = True

print(bfs(n, k))