from collections import deque

def solution(x, y, n):
    answer = 0
    
    visited = [False] * (y + 1)
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, 0))
        visited[x] = True
        
        while queue:
            x, cnt = queue.popleft()
            
            if x == y:
                return cnt
            
            for nx in (x + n, x * 2, x * 3):
                if 0 <= nx <= y and not visited[nx]:
                    visited[nx] = True
                    queue.append((nx, cnt + 1))
        
        return -1
    
    return bfs(x, y)