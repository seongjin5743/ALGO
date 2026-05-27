from collections import deque

def solution(maps):
    answer = []
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True
        cnt = int(maps[y][x])
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx].isdigit():
                    queue.append((nx, ny))
                    visited[ny][nx] = True
                    cnt += int(maps[ny][nx])
        return cnt
                               
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and maps[y][x].isdigit():
                answer.append(bfs(x, y))
                               
            
    return sorted(answer) if answer else [-1]