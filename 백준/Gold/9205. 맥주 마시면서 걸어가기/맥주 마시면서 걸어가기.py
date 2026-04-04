import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    home_x, home_y = map(int, input().split())

    convi = []
    for _ in range(n):
        x, y = map(int, input().split())
        convi.append((x, y))

    festi_x, festi_y = map(int, input().split())

    visited = [False] * n

    def bfs(x, y, thirsty):
        queue = deque()
        queue.append((x, y, 0, thirsty))

        while queue:
            x, y, dis, thirsty = queue.popleft()

            if abs(x - festi_x) + abs(y - festi_y) <= 1000:
                print('happy')
                return

            for i in range(n):
                if not visited[i]:
                    c_x, c_y = convi[i]

                    if abs(x - c_x) + abs(y - c_y) <= 1000:
                        visited[i] = True
                        queue.append((c_x, c_y, 0, False))

        print('sad')
        return

    bfs(home_x, home_y, False)