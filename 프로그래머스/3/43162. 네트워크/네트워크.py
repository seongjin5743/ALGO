from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False]  *  n
    
    def bfs(x):
        queue = deque()
        queue.append(x)
        visited[x] = True
        
        while queue:
            i = queue.popleft()
            for num in range(n):
                if computers[i][num] and not visited[num]:
                    queue.append(num)
                    visited[num] = True
                    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer