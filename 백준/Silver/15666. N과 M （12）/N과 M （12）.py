n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
out = []
visited = [False] * n


def recur(num):
    check = 0
    if len(out) == m:
        print(*out)
        return
    
    for i in range(num, n):
        if check != data[i]:
            out.append(data[i])
            check = data[i]
            recur(i)
            out.pop()
recur(0)