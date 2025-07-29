from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

# 상하좌우 방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    maze[x][y] = 0  # 방문 처리
    area_size = 1   # 시작점 포함

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = 0  # 방문 처리
                area_size += 1

    return area_size

count = 0
sizes = []

for i in range(n):
    for j in range(m):
        if maze[i][j] == 1:
            count += 1
            sizes.append(bfs(i, j))

print(count)
print(max(sizes) if sizes else 0)
