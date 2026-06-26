from collections import deque

def solution(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    n, m = len(maps[0]), len(maps)
    visited = [[False] * n for _ in range(m)]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True
        
        while queue:
            x, y = queue.popleft()
            
            if x == n - 1 and y == m - 1:
                return maps[m - 1][n - 1]
               
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx] and maps[ny][nx] == 1:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1
        return -1
    return bfs(0,0)