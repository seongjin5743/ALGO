n, k = map(int, input().split())

standings = []

for _ in range(n):
    num, g, s, b = map(int, input().split())
    standings.append((num, g, s, b))

target = []
for standing in standings:
    if standing[0] == k:
        target = standing
        break

rank = 1

for standing in standings:
    if (standing[1] > target[1]) or \
    (standing[1] == target[1] and standing[2] > target[2]) or \
    (standing[1] == target[1] and standing[2] == target[2] and standing[3] > target[3]):
        rank += 1

print(rank)