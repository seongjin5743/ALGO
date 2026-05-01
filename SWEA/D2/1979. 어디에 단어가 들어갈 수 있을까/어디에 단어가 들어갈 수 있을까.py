T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    
    answer = 0

    for y in range(n):
        for x in range(n - m + 1):
            if all(maze[y][x+i] == 1 for i in range(m)):
                if (x == 0 or maze[y][x-1] == 0) and (x + m == n or maze[y][x+m] == 0):
                    answer += 1

    for x in range(n):
        for y in range(n - m + 1):
            if all(maze[y+i][x] == 1 for i in range(m)):
                if (y == 0 or maze[y-1][x] == 0) and (y + m == n or maze[y+m][x] == 0):
                    answer += 1

    print(f'#{t} {answer}')