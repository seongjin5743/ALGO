n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
out = []
visited = [False] * n

def recur():
    check = 0
    if len(out) == m:
        print(*out)
        return
    for i in range(n):
        if check != data[i] and not visited[i]:
            out.append(data[i])
            visited[i] = True
            check = data[i]
            recur()
            visited[i] = False
            out.pop()

recur()