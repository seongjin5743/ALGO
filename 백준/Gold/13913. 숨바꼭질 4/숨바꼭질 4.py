from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001
prev = [-1] * 100001

def bfs(x, to):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        now = queue.popleft()
        if now == to:
            break
        
        for nx in ([now * 2, now - 1, now + 1]):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                prev[nx] = now
                queue.append(nx)

bfs(n, k)

path = []
current = k

while current != -1:
    path.append(current)
    current = prev[current]

path.reverse()

print(len(path) - 1)
print(*path)