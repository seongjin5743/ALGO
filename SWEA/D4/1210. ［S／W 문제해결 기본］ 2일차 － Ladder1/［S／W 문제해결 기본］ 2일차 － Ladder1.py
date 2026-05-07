from collections import deque

for t in range(1, 11):
    T = int(input())
    maze = [list(map(int, input().split())) for _ in range(100)]

    dx = [0, 1, -1]
    dy = [-1, 0, 0]

    s_x, s_y = 0, 0

    for y in range(100):
        for x in range(100):
            if maze[y][x] == 2:
                s_x, s_y = x, y

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        move_check = [[False] * 100 for _ in range(100)]
        move_check[y][x] = True

        while queue:
            x, y = queue.popleft()

            if y == 0:
                return x

            moved = False

            for i in range(1, 3):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < 100 and 0 <= ny < 100:
                    if maze[ny][nx] == 1 and not move_check[ny][nx]:
                        queue.append((nx, ny))
                        move_check[ny][nx] = True
                        moved = True
                        break

            if not moved:
                nx, ny = x + dx[0], y + dy[0]

                if 0 <= ny < 100:
                    queue.append((nx, ny))
                    move_check[ny][nx] = True

    answer = bfs(s_x, s_y)
    print(f"#{t} {answer}")