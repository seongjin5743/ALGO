from collections import deque

for t in range(1, 11):
    n, m = map(int, input().split())
    graph = [[] for _ in range(100)]
    visited = [False] * 100
    
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        graph[lst[i]].append(lst[i + 1])

    def bfs(x):
        queue = deque()
        queue.append(x)
        visited[x] = True

        while queue:
            x = queue.popleft()
            if x == 99:
                return 1
            for num in graph[x]:
                if not visited[num]:
                    queue.append(num)
                    visited[num] = True
        return 0
    answer = bfs(0)
    print(f"#{t} {answer}")