import heapq

T = int(input())

for t in range(1, T + 1):
    N, E = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)]
    dis = [1e6] * (N + 1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
    

    def dij(start):
        queue = []
        heapq.heappush(queue, (0, start))
        dis[start] = 0

        while queue:
            dist, now = heapq.heappop(queue)

            if dis[now] < dist:
                continue

            for n_dis, n_now in graph[now]:
                if dist + n_dis < dis[n_now]:
                    dis[n_now] = dist + n_dis
                    heapq.heappush(queue, (dis[n_now], n_now))
    dij(0)
    print(f'#{t} {dis[N]}')