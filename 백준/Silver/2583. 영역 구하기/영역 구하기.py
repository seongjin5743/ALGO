m, n, k = map(int, input().split())

dot = []
for _ in range(k):
    d = list(map(int, input().split()))
    dot.append(d)

maze = [[0] * n for _ in range(m)]

for i in range(k):
    x, y, x1, y1 = dot[i][0], dot[i][1], dot[i][2], dot[i][3]
    for row in range(y, y1):
        for col in range(x, x1):
            maze[row][col] = 1

from collections import deque

visited = [[False] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if not visited[ny][nx] and maze[ny][nx] == 0:
                cnt += 1
                visited[ny][nx] = True
                queue.append((nx, ny))
    return cnt

count = 0
answer = []


for y in range(m):
    for x in range(n):
        if not visited[y][x] and maze[y][x] == 0:
            answer.append(bfs(x, y))
            count += 1

print(count)
answer.sort()
print(*answer)