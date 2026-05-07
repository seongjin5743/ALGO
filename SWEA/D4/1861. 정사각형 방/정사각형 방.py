T = int(input())

for t in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    result_num = 0
    result_cnt = 0

    for y in range(n):
        for x in range(n):

            cnt = 1
            cx, cy = x, y

            while True:
                move = False

                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]

                    if 0 <= nx < n and 0 <= ny < n:
                        if maze[cy][cx] + 1 == maze[ny][nx]:
                            cnt += 1
                            cx, cy = nx, ny
                            move = True
                            break

                if not move:
                    break

            if cnt > result_cnt:
                result_cnt = cnt
                result_num = maze[y][x]

            elif cnt == result_cnt:
                result_num = min(result_num, maze[y][x])

    print(f"#{t} {result_num} {result_cnt}")