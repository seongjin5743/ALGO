from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 'S':
                s_x, s_y = x, y
            if maps[y][x] == 'L':
                l_x, l_y = x, y
            if maps[y][x] == 'E':
                e_x, e_y = x, y

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    def bfs(x, y, target):
        visited = [[False] * m for _ in range(n)]
        queue = deque([(x, y, 0)])
        visited[y][x] = True

        while queue:
            x, y, cnt = queue.popleft()

            if maps[y][x] == target:
                return cnt

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[ny][nx] and maps[ny][nx] != 'X':
                        visited[ny][nx] = True
                        queue.append((nx, ny, cnt + 1))

        return -1

    to_lever = bfs(s_x, s_y, 'L')
    if to_lever == -1:
        return -1

    to_exit = bfs(l_x, l_y, 'E')
    if to_exit == -1:
        return -1

    return to_lever + to_exit