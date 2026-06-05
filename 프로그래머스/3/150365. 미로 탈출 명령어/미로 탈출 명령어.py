import sys
sys.setrecursionlimit(3000)

def solution(n, m, x, y, r, c, k):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    temp = ['d', 'l', 'r', 'u']
    
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    
    shortest_dist = abs(x - r) + abs(y - c)
    if shortest_dist > k or (k - shortest_dist) % 2 == 1:
        return "impossible"
        
    alpha = []
    is_found = False

    def dfs(x, y, cnt, answer):
        nonlocal is_found
        
        if is_found:
            return
            
        if abs(x - r) + abs(y - c) > k - cnt:
            return
            
        if cnt == k:
            if x == r and y == c:
                alpha.append(answer)
                is_found = True
            return
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx, ny, cnt + 1, answer + temp[i])

    dfs(x, y, 0, "")
    
    return alpha[0] if alpha else "impossible"