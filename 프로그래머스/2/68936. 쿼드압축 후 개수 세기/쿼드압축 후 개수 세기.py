def solution(arr):
    answer = [0, 0]
    
    def dfs(x1, x2, y1, y2):
        all_zeros = all(arr[y][x] == 0 for y in range(y1, y2 + 1) for x in range(x1, x2 + 1))
        all_ones = all(arr[y][x] == 1 for y in range(y1, y2 + 1) for x in range(x1, x2 + 1))
        if all_zeros:
            answer[0] += 1
        elif all_ones:
            answer[1] += 1
        else:
            x_mid = (x1 + x2) // 2
            y_mid = (y1 + y2) // 2
            
            dfs(x1, x_mid, y1, y_mid)
            dfs(x1, x_mid, y_mid + 1, y2)
            dfs(x_mid + 1, x2, y1, y_mid)
            dfs(x_mid + 1, x2, y_mid + 1, y2)
                
    dfs(0, len(arr) - 1, 0, len(arr) - 1)
    return answer