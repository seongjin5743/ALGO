from collections import deque

def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y, 1))
        visited[y][x] = True
        while queue:
            x, y, answer = queue.popleft()
            
            if x == len(maps[0]) - 1 and y == len(maps) - 1:
                return answer
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < len(maps[0]) and 0<= ny < len(maps) and not visited[ny][nx] and maps[y][x] == 1:
                    queue.append((nx, ny, answer + 1))
                    visited[ny][nx] = True
        return -1
    return bfs(0,0)