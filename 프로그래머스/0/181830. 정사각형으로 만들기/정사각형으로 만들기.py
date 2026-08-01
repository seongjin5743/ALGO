def solution(arr):
    rows, cols = len(arr), len(arr[0])
    
    if rows == cols:
        return arr
    
    if rows > cols:
        return [row + [0] * (rows - cols) for row in arr]
    
    return arr + [[0] * cols for _ in range(cols - rows)]