from collections import deque

def solution(board):
    answer = -1
    
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    s_x, s_y = 0, 0
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 'R':
                s_x, s_y = x, y
                break
                
    queue = deque()
    queue.append((s_x, s_y, 0))
    visited[s_y][s_x] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if board[y][x] == 'G':
            answer = cnt
            break
        
        for i in range(4):
            nx, ny = x, y

            while True:

                next_nx = nx + dx[i]
                next_ny = ny + dy[i]

                if not (0 <= next_nx < len(board[0]) and 0 <= next_ny < len(board)) or board[next_ny][next_nx] == 'D':
                    break

                nx, ny = next_nx, next_ny
                
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, cnt + 1))
            
    return answer