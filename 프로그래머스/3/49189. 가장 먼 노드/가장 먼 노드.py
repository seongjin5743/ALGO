from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    distance = [-1] * (n + 1)
    
    queue = deque([1])
    distance[1] = 0
    
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if distance[nxt] == -1:
                distance[nxt] = distance[cur] + 1
                queue.append(nxt)
    
    max_dist = max(distance)
    return distance.count(max_dist)