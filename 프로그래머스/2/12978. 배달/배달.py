import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    distance = [float('inf')] * (N + 1)
    distance[1] = 0

    queue = [(0, 1)]

    while queue:
        dist, now = heapq.heappop(queue)
        
        if dist > distance[now]:
            continue
        
        for nxt, cost in graph[now]:
            n_dist = dist + cost
            
            if n_dist < distance[nxt]:
                distance[nxt] = n_dist
                heapq.heappush(queue, (n_dist, nxt))

    return sum(1 for d in distance[1:] if d <= K)