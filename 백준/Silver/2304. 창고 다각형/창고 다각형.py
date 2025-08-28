n = int(input())

buildings = []
for _ in range(n):
    x, y = map(int, input().split())
    buildings.append((x, y))

buildings.sort(key= lambda x: x[0])

max_height = 0
max_idx = 0
for i, (x, y) in enumerate(buildings):
    if y > max_height:
        max_height = y
        max_idx = i

answer = 0

current_height = buildings[0][1]
current_x = buildings[0][0]
for i in range(1, max_idx + 1):
    if buildings[i][1] >= current_height:
        answer += (buildings[i][0] - current_x) * current_height
        current_height = buildings[i][1]
        current_x = buildings[i][0]

current_height = buildings[-1][1]
current_x = buildings[-1][0]
for i in range(n - 2, max_idx - 1, -1):
    if buildings[i][1] >= current_height:
        answer += (current_x - buildings[i][0]) * current_height
        current_height = buildings[i][1]
        current_x = buildings[i][0]

answer += max_height

print(answer)