from collections import deque

n = int(input())

maze = []
for _ in range(n):
    ma = list(input())
    maze.append(ma)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y, visited):
    queue = deque()

    queue.append((x, y))
    visited[x][y] = True

    color = maze[x][y]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not visited[nx][ny] and maze[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

count = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited)
            count += 1


j_count = 0
visited = [[False] * n for _ in range(n)]
maze = [['R' if c == 'G' else c for c in row] for row in maze]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited)
            j_count += 1
print(count, j_count)