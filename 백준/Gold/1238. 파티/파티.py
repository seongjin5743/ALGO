import heapq

n, m, x = map(int, input().split())

graph1 = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]

INF = int(1e9)
times1 = [INF] * (n + 1)
times2 = [INF] * (n + 1)

for _ in range(m):
    start, to, time = map(int, input().split())
    graph1[start].append((to, time))
    graph2[to].append((start, time))


def short1(start):
    h = []
    heapq.heappush(h, (0, start))
    times1[start] = 0

    while h:
        ti, now = heapq.heappop(h)

        if times1[now] < ti:
            continue

        for to, time in graph1[now]:
            cost = time + ti
            if cost < times1[to]:
                times1[to] = cost
                heapq.heappush(h, (cost, to))

def short2(to):
    h = []
    heapq.heappush(h, (0, to))
    times2[to] = 0

    while h:
        ti, now = heapq.heappop(h)

        if times2[now] < ti:
            continue

        for to, time in graph2[now]:
            cost = time + ti
            if cost < times2[to]:
                times2[to] = cost
                heapq.heappush(h, (cost, to))

short1(x)
short2(x)

max_num = 0
for i in range(1, n + 1):
    if times1[i] != INF and times2[i] != INF:
        max_num = max(max_num, times1[i] + times2[i])
print(max_num)