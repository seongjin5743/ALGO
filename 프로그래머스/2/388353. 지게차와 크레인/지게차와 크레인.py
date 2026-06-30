from collections import deque

def solution(storage, requests):
    answer = 0
    
    n, m = len(storage), len(storage[0])
    
    padded_storage = [['.'] * (m + 2) for _ in range(n + 2)]
    
    for y in range(n):
        for x in range(m):
            padded_storage[y + 1][x + 1] = storage[y][x]
    storage = padded_storage
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(x, y, target):
        queue = deque()
        queue.append((x, y))
        visited[y][x] = True
        
        to_remove = []
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < m + 2 and 0 <= ny < n + 2 and not visited[ny][nx]:
                    if storage[ny][nx] == '.':
                        visited[ny][nx] = True
                        queue.append((nx, ny))
                    elif storage[ny][nx] == target:
                        visited[ny][nx] = True
                        to_remove.append((nx, ny))
                        
        for rx, ry in to_remove:
            storage[ry][rx] = '.'

    for request in requests:
        visited = [[False] * (m + 2) for _ in range(n + 2)]
        
        if len(request) == 1:
            bfs(0, 0, request)
        else:
            temp = request[0]
            for y in range(1, n + 1):
                for x in range(1, m + 1):
                    if storage[y][x] == temp:
                        storage[y][x] = '.'
                        
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if storage[y][x] != '.':
                answer += 1
                
    return answer