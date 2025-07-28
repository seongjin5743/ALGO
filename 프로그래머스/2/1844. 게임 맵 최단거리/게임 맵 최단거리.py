from collections import deque

def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                    continue
                    
                if maps[nx][ny] == 0:
                    continue
                    
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        return maps[-1][-1]
    
    result = bfs(0, 0)
    return -1 if result == 1 else result