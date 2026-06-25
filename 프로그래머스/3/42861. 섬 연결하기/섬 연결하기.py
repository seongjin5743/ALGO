import heapq

def solution(n, costs):
    graph = [[] for _ in range(n)]
    
    for x, y, cost in costs:
        graph[x].append((cost, y))
        graph[y].append((cost, x))
    
    
    visited = [False] * n
    queue = [(0, 0)]
    answer = 0
    
    while queue:
        cost, now = heapq.heappop(queue)
        
        if visited[now]:
            continue
        
        visited[now] = True
        answer += cost
        
        for n_cost, n in graph[now]:
            if not visited[n]:
                heapq.heappush(queue, (n_cost, n))

    return answer