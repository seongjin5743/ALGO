T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [[0] * N for _ in range(N)]
    dx = [1, 0 ,-1, 0]
    dy = [0, 1, 0, -1]
    x, y = 0, 0
    count = 0
    for i in range(1, (N * N) + 1):
        maze[y][x] = i

        nx, ny = x + dx[count], y + dy[count]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or maze[ny][nx] != 0:
            count = (count + 1) % 4
            nx, ny = x + dx[count], y + dy[count]

        x, y = nx, ny
    print(f'#{test_case}')
    for row in maze:
        print(' '.join(map(str, row)))