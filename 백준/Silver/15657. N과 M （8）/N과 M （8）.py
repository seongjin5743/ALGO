n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
out = []

def dfs(num):
    if len(out) == m:
        print(' '.join(map(str, out)))
        return
    
    for i in range(num, n):
        out.append(data[i])
        dfs(i)
        out.pop()

dfs(0)