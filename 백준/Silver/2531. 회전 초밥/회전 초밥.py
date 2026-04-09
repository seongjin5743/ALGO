import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]
sushi += sushi

answer = 0

for i in range(n):
    window = sushi[i:i+k]
    kinds = set(window)

    if c not in kinds:
        answer = max(answer, len(kinds) + 1)
    else:
        answer = max(answer, len(kinds))

print(answer)