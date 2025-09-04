from collections import deque

n, l, r = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    union = [(x, y)]
    population = maze[y][x]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and l <= abs(maze[y][x] - maze[ny][nx]) <= r:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    population += maze[ny][nx]

    if len(union) > 1:
        n_population = population // len(union)
        for ux, uy in union:
            maze[uy][ux] = n_population
        return True
    
    return False


days = 0
while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                if bfs(x, y, visited):
                    moved = True

    if not moved:
        break
    days += 1

print(days)