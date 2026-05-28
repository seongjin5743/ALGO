from collections import deque


def solution(n, wires):
    answer = 100
    graph = [[] for _ in range(n + 1)]
    
    for cut_a, cut_b in wires:
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        
        def bfs(x):
            queue = deque()
            queue.append(x)
            visited[x] = True
            cnt = 0
            while queue:
                x = queue.popleft()
                
                for num in graph[x]:
                    if not visited[num]:
                        queue.append(num)
                        visited[num] = True
                        cnt += 1
            return cnt
        
        for a, b in wires:
            if (a, b) == (cut_a, cut_b):
                continue

            graph[a].append(b)
            graph[b].append(a)
        
        qwer = []
        for i in range(1, n + 1):
            if not visited[i]:
                qwer.append(bfs(i))
        answer = min(answer, abs(qwer[1] - qwer[0]))
        
    return answer