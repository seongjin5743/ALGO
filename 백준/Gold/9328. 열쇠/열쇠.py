from collections import deque
import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    n, m = map(int, input().split())
    maze = [list(input().strip()) for _ in range(n)]
    keys = set(input().strip())
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    visited = [[False]*m for _ in range(n)]
    doors = {chr(i): [] for i in range(65,91)}
    
    queue = deque()

    for y in range(n):
        for x in range(m):
            if y==0 or y==n-1 or x==0 or x==m-1:
                if maze[y][x] != '*':
                    queue.append((x,y))
                    visited[y][x] = True
    
    count = 0
    while queue:
        x, y = queue.popleft()
        cell = maze[y][x]

        if cell == '$':
            count += 1
            maze[y][x] = '.'

        if 'a' <= cell <= 'z' and cell not in keys:
            keys.add(cell)
            for door_x, door_y in doors[cell.upper()]:
                queue.append((door_x, door_y))
            doors[cell.upper()] = []

        if 'A' <= cell <= 'Z':
            if cell.lower() not in keys:
                doors[cell].append((x,y))
                continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and maze[ny][nx] != '*':
                visited[ny][nx] = True
                queue.append((nx, ny))

    print(count)