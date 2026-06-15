def solution(m, n, board):
    answer1 = 0
    board = [list(row) for row in board]
    
    while True:
        matched = set()
        
        for y in range(m - 1):
            for x in range(n - 1):
                color = board[y][x]
                if color == 0:
                    continue
                
                if (board[y + 1][x] == color and 
                    board[y][x + 1] == color and 
                    board[y + 1][x + 1] == color):
                    matched.update([(y, x), (y + 1, x), (y, x + 1), (y + 1, x + 1)])

        if not matched:
            break
            
        answer1 += len(matched)
        for y, x in matched:
            board[y][x] = 0

        for j in range(n):
            stack = [board[i][j] for i in range(m) if board[i][j] != 0]
            for i in range(m - 1,-1,-1):
                board[i][j] = stack.pop() if stack else 0
                    
    return answer1