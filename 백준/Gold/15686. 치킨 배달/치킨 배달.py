from itertools import combinations

n, k = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house = []

for y in range(n):
    for x in range(n):
        if maze[y][x] == 2:
            maze[y][x] = 0
            chicken.append([y, x])
        if maze[y][x] == 1:
            house.append([y, x])

def distance(c_indexs):
    distance = 0
    for h_y, h_x in house:
        min_distance = int(1e9)
        for c_y, c_x in c_indexs:
            min_distance = min(min_distance, abs(c_y - h_y) + abs(c_x - h_x))
        distance += min_distance

    return distance

min_num = int(1e9)

for comb in combinations(chicken, k):
    min_num = min(min_num, distance(comb))

print(min_num)