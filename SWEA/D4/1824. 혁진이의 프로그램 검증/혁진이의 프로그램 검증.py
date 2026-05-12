from collections import deque

T = int(input())

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for t in range(1, T + 1):
    R, C = map(int, input().split())
    maze = [input().strip() for _ in range(R)]
    
    visited = [[[[False] * 4 for _ in range(16)] for _ in range(C)] for _ in range(R)]
    
    queue = deque([(0, 0, 0, 0)])
    visited[0][0][0][0] = True
    
    answer = "NO"
    
    while queue:
        y, x, num, d = queue.popleft()
        
        char = maze[y][x]
        
        next_ds = [d]
        
        if char == '<': next_ds = [1]
        elif char == '>': next_ds = [0]
        elif char == '^': next_ds = [3]
        elif char == 'v': next_ds = [2]
        elif char == '_': next_ds = [0] if num == 0 else [1]
        elif char == '|': next_ds = [2] if num == 0 else [3]
        elif char == '?': next_ds = [0, 1, 2, 3]
        elif char == '@':
            answer = "YES"
            break
        elif '0' <= char <= '9':
            num = int(char)
        elif char == '+':
            num = (num + 1) % 16
        elif char == '-':
            num = (num - 1) % 16

        for i in next_ds:
            ny = (y + dy[i]) % R
            nx = (x + dx[i]) % C
            
            if not visited[ny][nx][num][i]:
                visited[ny][nx][num][i] = True
                queue.append((ny, nx, num, i))
                
    print(f'#{t} {answer}')