import sys
input = sys.stdin.readline

n = int(input())

rank = [int(input()) for _ in range(n)]

rank.sort()

answer = 0
for i in range(n):
    answer += abs((i + 1) - rank[i])

print(answer)