import sys
input = sys.stdin.readline

n = int(input())

n = 1000 - n
coins = [500, 100, 50, 10, 5, 1]

answer = 0

for coin in coins:
    if n >= coin:
        i = n // coin
        answer += i
        n -= coin * i

print(answer)