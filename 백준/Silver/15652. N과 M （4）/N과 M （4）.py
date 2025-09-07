import sys

input = sys.stdin.readline

n, m = map(int, input().split())

rs = []

def recur(num):
    if len(rs) == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(num, n + 1):

        rs.append(i)
        recur(i)
        rs.pop()

recur(1)