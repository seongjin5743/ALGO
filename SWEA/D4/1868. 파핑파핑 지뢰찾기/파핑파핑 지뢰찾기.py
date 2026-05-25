from collections import deque

T = int(input())

# 8방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for t in range(1, T + 1):
    n = int(input())
    maze = [list(input().strip()) for _ in range(n)]
    board = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if maze[y][x] == '*':
                board[y][x] = -1
                continue

            cnt = 0

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if maze[ny][nx] == '*':
                        cnt += 1

            board[y][x] = cnt

    visited = [[False] * n for _ in range(n)]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True

        while queue:
            x, y = queue.popleft()

            if board[y][x] != 0:
                continue

            for i in range(8):
                nx ,ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[ny][nx] and board[ny][nx] != -1:
                        visited[ny][nx] = True
                        queue.append((nx, ny))

    answer = 0

    for y in range(n):
        for x in range(n):
            if board[y][x] == 0 and not visited[y][x]:
                bfs(x, y)
                answer += 1

    for y in range(n):
        for x in range(n):
            if board[y][x] > 0 and not visited[y][x]:
                answer += 1

    print(f"#{t} {answer}")