import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True
    melt = []

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = True
                if maze[ny][nx] == 0:
                    q.append((ny, nx))
                else:
                    melt.append((ny, nx))
    
    for y, x in melt:
        maze[y][x] = 0
        
    return len(melt)

time = 0
cheese = 0

while True:
    current_cheese = sum(row.count(1) for row in maze)
    if current_cheese == 0:
        break
        
    cheese = current_cheese
    bfs()
    time += 1

print(time)
print(cheese)