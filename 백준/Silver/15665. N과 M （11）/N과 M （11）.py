n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
out = []

def recur():
    check = 0
    if len(out) == m:
        print(*out)
        return
    
    for i in range(n):
        if data[i] != check:
            check = data[i]
            out.append(data[i])
            recur()
            out.pop()
recur()