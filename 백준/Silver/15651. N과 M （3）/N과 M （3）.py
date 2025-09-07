import sys

input = sys.stdin.readline

n, m = map(int, input().split())

rs = []

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(1, n + 1):
        rs.append(i)
        recur(num + 1)
        rs.pop()

recur(0)