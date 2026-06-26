import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    
    for a, b, time in road:
        graph[a].append((time, b))
        graph[b].append((time, a))
    
    distance = [1e9] * (N + 1)
    
    distance[1] = 0
    
    queue = [(0, 1)]
    
    while queue:
        dis, now = heapq.heappop(queue)

        for n_dis, n in graph[now]:
            nxt_dis = dis + n_dis
            if nxt_dis < distance[n]:
                distance[n] = nxt_dis
                heapq.heappush(queue, (nxt_dis, n))
    count = 0
    for d in distance:
        if d <= K:
            count += 1
    return count