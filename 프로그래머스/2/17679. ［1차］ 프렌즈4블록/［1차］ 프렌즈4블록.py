def solution(m, n, board):
    answer1 = 0
    board = [list(row) for row in board]
    while True:
        index = set()
        for y in range(m - 1):
            for x in range(n - 1):
                color = board[y][x]
                if color == '-':
                    continue
                
                if board[y + 1][x] == color and board[y][x + 1] == color and board[y + 1][x + 1] == color:
                    index.add((x, y))
                    index.add((x + 1, y))
                    index.add((x, y + 1))
                    index.add((x + 1, y + 1))

        if not index:
            break
            
        answer1 += len(index)
        for x, y in index:
            board[y][x] = '-'
                    
        for x in range(n):
            for y in range(m - 1, -1, -1):
                if board[y][x] == '-':
                    ny = y - 1
                    while ny >= 0 and board[ny][x] == '-':
                        ny -= 1
                    
                    if ny >= 0:
                        board[y][x] = board[ny][x]
                        board[ny][x] = '-'
    return answer1