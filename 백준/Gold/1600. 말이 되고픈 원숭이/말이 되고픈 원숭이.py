from collections import deque

k = int(input())

w, h = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(h)]

visited = [[[False] * (k+1) for _ in range(w)] for _ in range(h)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

h_dx = [1,2,2,1,-1,-2,-2,-1]
h_dy = [2,1,-1,-2,-2,-1,1,2]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0, 0))
    visited[y][x][0] = True

    while queue:
        x, y, count, nk = queue.popleft()

        if x == w - 1 and y == h - 1:
            return count

        if nk < k:
            for i in range(8):
                h_nx, h_ny = x + h_dx[i], y + h_dy[i]
                if 0 <= h_nx < w and 0 <= h_ny < h:
                    if not visited[h_ny][h_nx][nk+1] and maze[h_ny][h_nx] == 0:
                        visited[h_ny][h_nx][nk+1] = True
                        queue.append((h_nx, h_ny, count+1, nk+1))

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny][nx][nk] and maze[ny][nx] == 0:
                    visited[ny][nx][nk] = True
                    queue.append((nx, ny, count+1, nk))

    return -1

print(bfs(0, 0))