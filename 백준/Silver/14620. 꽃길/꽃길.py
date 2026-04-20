import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

visited = [[False] * n for _ in range(n)]

ans = 1e9

def recur(cnt, price):
    global ans
    if cnt == 3:
        ans = min(ans, price)
        return

    for x in range(1, n - 1):
        for y in range(1, n - 1):
            flag = False
            temp = 0
            cell = []

            for i in range(5):
                nx, ny = x + dx[i], y + dy[i]

                if visited[nx][ny]:
                    flag = True
                    break
                temp += arr[nx][ny]
                cell.append((nx, ny))
            
            if not flag:
                for cx, cy in cell:
                    visited[cx][cy] = True
                recur(cnt + 1, price + temp)
                for cx, cy in cell:
                    visited[cx][cy] = False

recur(0,0)
print(ans)