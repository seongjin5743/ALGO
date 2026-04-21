import sys
input = sys.stdin.readline

board = [input().split() for _ in range(5)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = set()

def dfs(x, y, num):
    if len(num) == 6:
        result.add(num)
        return
    
    for i in range(4):
        nx, ny = x+ dx[i], y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + board[ny][nx])

for y in range(5):
    for x in range(5):
        dfs(x, y, board[y][x])

print(len(result))