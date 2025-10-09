import sys

input = sys.stdin.readline

n = int(input())

people = []
for _ in range(n):
    p = list(input().split())
    people.append(p)

people.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for p in people:
    print(p[0])