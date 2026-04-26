T = int(input())

for t in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [1,1,-1,-1]
    dy = [1,-1,-1,1]

    def dfs(x, y, dir, lst, start_x, start_y):
        global answer

        for i in [dir, dir + 1]:
            if i >= 4:
                continue

            nx ,ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if nx == start_x and ny == start_y and i == 3:
                    answer = max(answer, len(lst))
                    return

                if not visited[ny][nx] and maze[ny][nx] not in lst:
                    visited[ny][nx] = True
                    lst.append(maze[ny][nx])
                    dfs(nx, ny, i, lst, start_x, start_y)
                    lst.pop()
                    visited[ny][nx] = False
                    
    answer = -1

    for y in range(n):
        for x in range(n):
            visited = [[False] * n for _ in range(n)]
            visited[y][x] = True
            dfs(x, y, 0, [maze[y][x]], x, y)

    print(f'#{t} {answer}')