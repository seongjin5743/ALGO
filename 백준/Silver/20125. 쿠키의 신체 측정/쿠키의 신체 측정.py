n = int(input())

maze = [list(input()) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

a_x, a_y = 0, 0

l_arm, r_arm, back, l_leg, r_leg = 0,0,0,0,0

for y in range(n):
    for x in range(n):
        count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maze[ny][nx] == '*':
                count += 1
        if count == 4:
            a_x, a_y = x, y
            break

l_arm_count = 1
while True:
    if 0 <= a_x - l_arm_count < n and maze[a_y][a_x - l_arm_count] == '*':
        l_arm += 1
        l_arm_count += 1
    else:
        break

r_arm_count = 1
while True:
    if 0 <= a_x + r_arm_count < n and maze[a_y][a_x + r_arm_count] == '*':
        r_arm += 1
        r_arm_count += 1
    else:
        break

back_count = 1
while True:
    if 0 <= a_y + back_count < n and maze[a_y + back_count][a_x] == '*':
        back += 1
        back_count += 1
    else:
        break

l_leg_index_x, l_leg_index_y = a_x - 1, a_y + back
l_leg_count = 1
while True:
    if 0 <= l_leg_index_y + l_leg_count < n and maze[l_leg_index_y + l_leg_count][l_leg_index_x] == '*':
        l_leg += 1
        l_leg_count += 1
    else:
        break

r_leg_index_x, r_leg_index_y = a_x + 1, a_y + back
r_leg_count = 1
while True:
    if  0 <= r_leg_index_y + r_leg_count < n and maze[r_leg_index_y + r_leg_count][r_leg_index_x] == '*':
        r_leg += 1
        r_leg_count += 1
    else:
        break

print(a_y + 1, a_x + 1)
print(l_arm, r_arm, back, l_leg, r_leg)