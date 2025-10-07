import sys

input = sys.stdin.readline

n = int(input())

dic = {}

for _ in range(n):
    name, a = input().split()

    if a == 'enter':
        dic[name] = 1
    else:
        dic[name] -= 1

for name in sorted(dic.keys(), reverse=True):
    if dic[name]:
        print(name)