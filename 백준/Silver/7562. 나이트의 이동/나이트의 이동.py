from collections import deque

n = int(input())

for _ in range(n):
    l = int(input())

    x, y = map(int, input().split())
    fx, fy = map(int, input().split())

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    visited = [[False] * l for _ in range(l)]
    
    def bfs(x, y, visited, count):
        queue = deque()
        queue.append((x,y,count))
        visited[x][y] = True
        
        while queue:
            x, y, count = queue.popleft()

            if x == fx and y == fy:
                return count
            
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or nx >= l or ny >= l:
                    continue

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, count + 1))

    print(bfs(x, y, visited, 0))
    