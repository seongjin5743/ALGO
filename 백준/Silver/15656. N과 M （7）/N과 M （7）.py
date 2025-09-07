import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
rs = []

def recur():
    if len(rs) == m:
        print(*rs)
        return
    
    for i in range(n):
        rs.append(data[i])
        recur()
        rs.pop()

recur()