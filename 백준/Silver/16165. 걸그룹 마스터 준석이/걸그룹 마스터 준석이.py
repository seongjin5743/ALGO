import sys

input = sys.stdin.readline

n, m = map(int, input().split())

girlgroup = {}

for _ in range(n):
    gg = input().strip()
    num = int(input())
    gl = []
    for _ in range(num):
        gn = input().strip()
        gl.append(gn)
    gl.sort()
    girlgroup[gg] = gl

for _ in range(m):
    name = input().strip()
    num = int(input())
    if num == 0:
        for member in girlgroup[name]:
            print(member)
    else:
        for group, members in girlgroup.items():
            if name in members:
                print(group)
                break