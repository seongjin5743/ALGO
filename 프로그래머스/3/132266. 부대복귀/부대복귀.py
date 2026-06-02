from collections import deque

def solution(n, roads, sources, destination):

    graph = [[] for _ in range(n + 1)]

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dist = [-1] * (n + 1)

    queue = deque([destination])
    dist[destination] = 0

    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                queue.append(nx)

    return [dist[s] for s in sources]