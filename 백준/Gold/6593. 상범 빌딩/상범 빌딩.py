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
        try:
            input()
        except:
            pass

    visited = [[[False]*c for _ in range(r)] for _ in range(l)]

    for z in range(l):
        for y in range(r):
            for x in range(c):
                if maze[z][y][x] == 'S':
                    start = (x, y, z)

    def bfs(sx, sy, sz):
        queue = deque()
        queue.append((sx, sy, sz, 0))
        visited[sz][sy][sx] = True

        while queue:
            x, y, z, cnt = queue.popleft()
            if maze[z][y][x] == 'E':
                return f'Escaped in {cnt} minute(s).'

            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
                if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l:
                    if not visited[nz][ny][nx] and maze[nz][ny][nx] in ('.', 'E'):
                        visited[nz][ny][nx] = True
                        queue.append((nx, ny, nz, cnt+1))

        return 'Trapped!'

    print(bfs(*start))