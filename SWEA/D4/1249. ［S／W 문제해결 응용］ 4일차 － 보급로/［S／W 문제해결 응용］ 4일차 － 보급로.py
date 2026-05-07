from collections import deque

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    def bfs(sx, sy):
        q = deque()
        q.append((sx, sy))

        distance = [[float('inf')] * N for _ in range(N)]
        distance[sx][sy] = 0

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    cost = distance[x][y] + maze[nx][ny]

                    if distance[nx][ny] > cost:
                        distance[nx][ny] = cost
                        q.append((nx, ny))

        return distance[N - 1][N - 1]
    
    answer = bfs(0, 0)

    print(f'#{t} {answer}')