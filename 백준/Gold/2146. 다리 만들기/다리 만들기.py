from collections import deque

n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, mark):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    maze[x][y] = mark

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if maze[nx][ny] == 1:
                    visited[nx][ny] = True
                    maze[nx][ny] = mark
                    queue.append((nx, ny))

mark = 2
for i in range(n):
    for j in range(n):
        if maze[i][j] == 1 and not visited[i][j]:
            bfs(i, j, mark)
            mark += 1

def bridge(start):
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(n):
            if maze[i][j] == start:
                queue.append((i, j))
                dist[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] > 0 and maze[nx][ny] != start:
                    return dist[x][y]
                if maze[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return float('inf')

answer = float('inf')
for k in range(2, mark):
    answer = min(answer, bridge(k))

print(answer)