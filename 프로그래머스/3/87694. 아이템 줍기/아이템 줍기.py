from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]

    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] = 1

    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                board[x][y] = 0

    q = deque()
    visited = [[False]*102 for _ in range(102)]

    q.append((characterX*2, characterY*2, 0))
    visited[characterX*2][characterY*2] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, dist = q.popleft()

        if x == itemX*2 and y == itemY*2:
            return dist // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 102 and 0 <= ny < 102:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))