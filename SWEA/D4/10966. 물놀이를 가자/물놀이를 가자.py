from collections import deque

T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    maze = [list(input().strip()) for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[-1] * m for _ in range(n)]
    
    queue = deque()

    for y in range(n):
        for x in range(m):
            if maze[y][x] == 'W':
                queue.append((x, y))
                dist[y][x] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((nx, ny))

    answer = 0

    for y in range(n):
        for x in range(m):
            answer += dist[y][x]

    print(f"#{t} {answer}")