import sys
input = sys.stdin.readline

n, m = map(int, input().split())

girlgroup = {}
member_to_group = {}

for _ in range(n):
    gg = input().strip()
    num = int(input())
    gl = [input().strip() for _ in range(num)]
    gl.sort()
    girlgroup[gg] = gl
    for g in gl:
        member_to_group[g] = gg

for _ in range(m):
    name = input().strip()
    num = int(input())
    if num == 0:
        for member in girlgroup[name]:
            print(member)
    else:
        print(member_to_group[name])