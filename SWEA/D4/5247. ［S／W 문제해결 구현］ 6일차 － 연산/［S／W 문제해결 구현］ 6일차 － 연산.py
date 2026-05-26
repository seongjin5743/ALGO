from collections import deque

T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())

    visited = [False] * 1000001

    def bfs(x):
        queue = deque()
        queue.append((x, 0))
        visited[x] = True

        while queue:
            x, cnt = queue.popleft()

            if x == m:
                return cnt

            for nx in (x + 1, x - 1, x * 2, x - 10):
                if 0 <= nx <= 1000000 and not visited[nx]:
                    queue.append((nx, cnt + 1))
                    visited[nx] = True
    answer = bfs(n)
    print(f'#{t} {answer}')