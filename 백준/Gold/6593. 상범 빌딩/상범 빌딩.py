from collections import deque
import sys

input = sys.stdin.readline

dz = [0, 0, 0, 0, 1, -1]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    maze = []
    for _ in range(l):
        floor = [list(input().strip()) for _ in range(r)]
        maze.append(floor)
        _ = input().strip()  # 층 사이의 빈 줄 처리

    visited = [[[False] * c for _ in range(r)] for _ in range(l)]

    def bfs(x, y, z):
        queue = deque([(x, y, z, 0)])
        visited[z][y][x] = True

        while queue:
            x, y, z, cnt = queue.popleft()
            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l and not visited[nz][ny][nx]:
                    if maze[nz][ny][nx] == '.':
                        visited[nz][ny][nx] = True
                        queue.append((nx, ny, nz, cnt + 1))
                    elif maze[nz][ny][nx] == 'E':
                        return f'Escaped in {cnt + 1} minute(s).'
        return 'Trapped!'

    found = False
    for z in range(l):
        for y in range(r):
            for x in range(c):
                if maze[z][y][x] == 'S':
                    print(bfs(x, y, z))
                    found = True
                    break
            if found:
                break
        if found:
            break