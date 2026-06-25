from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    
    visited = [False] * (n + 1)
    
    for x, y in vertex:
        graph[x].append(y)
        graph[y].append(x)

    answer = []
    
    def bfs(x):
        queue = deque()
        queue.append((x, 0))
        visited[x] = True
        
        while queue:
            x, cnt = queue.popleft()
            answer.append((x, cnt))
            for i in graph[x]:
                if not visited[i]:
                    queue.append((i, cnt + 1))
                    visited[i] = True
          
    bfs(1)
    
    max_dis = 0
    
    for x, dis in answer:
        max_dis = max(dis, max_dis)
    
    count = 0
    for x, dis in answer:
        if dis == max_dis:
            count += 1
    return count