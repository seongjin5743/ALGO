from collections import deque

def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y, 1))
        
        visited[y][x] = True
        
        while queue:
            x, y, num = queue.popleft()
            
            if x == m - 1 and y == n - 1:
                return num
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny, num + 1))
        return -1
    
    return bfs(0,0)