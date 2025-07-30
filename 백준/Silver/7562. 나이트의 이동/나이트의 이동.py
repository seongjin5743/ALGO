from collections import deque

n = int(input())

for _ in range(n):
    l = int(input())
    x, y = map(int, input().split())
    fx, fy = map(int, input().split())
    
    visited = [[False] * l for _ in range(l)]

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y, 0))
        visited[x][y] = True

        while queue:
            x, y, count = queue.popleft()

            if x == fx and y == fy:
                return count
            
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or ny >= l or nx >= l:
                    continue

                if not visited[nx][ny]:
                    queue.append((nx, ny,count + 1))
                    visited[nx][ny] = True
    print(bfs(x, y))