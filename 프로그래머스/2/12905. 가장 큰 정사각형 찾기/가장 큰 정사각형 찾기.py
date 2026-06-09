def solution(board):
    row = len(board)
    col = len(board[0])

    max_len = 0
    for r in range(row):
        for c in range(col):
            if board[r][c] == 1:
                max_len = 1
                break
        if max_len == 1:
            break

    for y in range(1, row):
        for x in range(1, col):
            if board[y][x] == 1:
                board[y][x] = min(board[y][x - 1], board[y - 1][x], board[y - 1][x - 1]) + 1
                
                if board[y][x] > max_len:
                    max_len = board[y][x]
                    
    return max_len ** 2