from collections import deque

def solution(board):
    N = len(board)
    INF = float('inf')
    visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    queue = deque()
    if board[1][0] != 1:
        queue.append((0, 1, 100, 0))
        visited[1][0][0] = 100
        
    if board[0][1] != 1:
        queue.append((1, 0, 100, 1))
        visited[0][1][1] = 100
    
    while queue:
        x, y, price, dir = queue.popleft()
        
        if x == N - 1 and y == N - 1:
            continue
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and board[ny][nx] != 1:
                next_price = price + 100 if i == dir else price + 600
                
                if next_price < visited[ny][nx][i]:
                    visited[ny][nx][i] = next_price
                    queue.append((nx, ny, next_price, i))
                    
    return min(visited[N-1][N-1])