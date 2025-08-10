import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

city_num, end_num = map(int, input().split())

INF = int(1e9)

distance = [INF] * (n + 1)


def short(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0

    while h:
        dis, now = heapq.heappop(h)

        if dis > distance[now]:
            continue

        for to, d in graph[now]:
            cost = dis + d
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(h, (cost, to))

short(city_num)

print(distance[end_num])