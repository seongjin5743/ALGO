n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


count = 0

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1

    cleaned = False
    for _ in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            r, c = nx, ny
            cleaned = True
            break

    if cleaned:
        continue

    back = (d + 2) % 4
    nx = r + dx[back]
    ny = c + dy[back]
    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1:
        r, c = nx, ny
    else:
        break

print(count)