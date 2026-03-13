import sys
from collections import deque

input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while True:
    l,r,c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    maze = []

    for _ in range(l):
        floor = [list(input().strip()) for _ in range(r)]
        maze.append(floor)
        _ = input().strip()
    
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]

    def bfs(x, y, z):
        queue = deque()
        queue.append((x, y, z, 0))
        visited[z][y][x] = True

        while queue:
            x, y, z, count = queue.popleft()
            
            if maze[z][y][x] == 'E':
                print(f'Escaped in {count} minute(s).')
                return

            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

                if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l:
                    if not visited[nz][ny][nx] and maze[nz][ny][nx] != '#':
                        queue.append((nx, ny, nz, count + 1))
                        visited[nz][ny][nx] = True
        print('Trapped!')

    for z in range(l):
        for y in range(r):
            for x in range(c):
                if maze[z][y][x] == 'S':
                    bfs(x,y,z)
                    break