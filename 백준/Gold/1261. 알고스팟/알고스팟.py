from collections import deque

m, n = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x,y,0))

    visited[y][x] = True

    while queue:
        x, y, count = queue.popleft()

        if x == m - 1 and y == n - 1:
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if maze[ny][nx] == 0:
                    queue.appendleft((nx,ny,count))
                    visited[ny][nx] = True
                else:
                    queue.append((nx,ny,count + 1))
                    visited[ny][nx] = True

print(bfs(0,0))