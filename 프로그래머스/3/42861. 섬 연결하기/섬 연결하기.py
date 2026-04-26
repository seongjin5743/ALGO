import heapq

def solution(n, costs):
    
    graph = [[] for _ in range(n)]
    
    for x, y, cost in costs:
        graph[x].append((cost, y))
        graph[y].append((cost, x))
    
    visited = [False] * n
    q = [(0, 0)]
    answer = 0
    
    while q:
        cost, now = heapq.heappop(q)
        
        if visited[now]:
            continue
        
        visited[now] = True
        answer += cost
        
        for next_cost, next_node in graph[now]:
            if not visited[next_node]:
                heapq.heappush(q, (next_cost, next_node))
    
    return answer