n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

count = 0
for i in range(len(coins)):
    if coins[i] <= k:
        count += k // coins[i]
        k -= (k // coins[i]) * coins[i]
    if k == 0:
        break
print(count)