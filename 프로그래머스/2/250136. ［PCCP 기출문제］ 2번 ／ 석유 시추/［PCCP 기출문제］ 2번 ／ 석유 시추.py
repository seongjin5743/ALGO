from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    visited = [[False] * m for _ in range(n)]
    oil = [0] * m

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True

        count = 1
        cols = set()
        cols.add(x)

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[ny][nx] and land[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append((nx, ny))
                        count += 1
                        cols.add(nx)

        return count, cols

    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and not visited[y][x]:
                count, cols = bfs(x, y)

                for col in cols:
                    oil[col] += count

    return max(oil)