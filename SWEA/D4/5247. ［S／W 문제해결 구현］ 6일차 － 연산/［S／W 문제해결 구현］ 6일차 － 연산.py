from collections import deque

T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())

    visited = [False] * 1000001

    def bfs():
        queue = deque([(n, 0)])
        visited[n] = True

        while queue:
            x, cnt = queue.popleft()

            if x == m:
                return cnt

            for nx in (x + 1, x - 1, x * 2, x - 10):
                if 0 <= nx <= 1000000 and not visited[nx]:
                    visited[nx] = True
                    queue.append((nx, cnt + 1))

    print(f'#{t} {bfs()}')