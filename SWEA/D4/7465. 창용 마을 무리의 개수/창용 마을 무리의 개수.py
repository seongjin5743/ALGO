from collections import deque

T = int(input())

for t in range(1, T + 1):

    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (n + 1)
    
    def bfs(x):
        queue = deque()
        visited[x] = True
        queue.append(x)

        while queue:
            x = queue.popleft()

            for nx in graph[x]:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append(nx)
    answer = 0

    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    print(f'#{t} {answer}')