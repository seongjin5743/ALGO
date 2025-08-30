import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

INF = int(1e9)

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

def short(start):
    h = []
    heapq.heappush(h, (0, start))

    distance[start] = 0

    while h:
        dis, now = heapq.heappop(h)

        if dis > distance[now]:
            continue

        for to, co in graph[now]:
            cost = dis + co
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(h, (cost, to))

short(1)

print(distance[n])