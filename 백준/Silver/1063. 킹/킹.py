import sys
input = sys.stdin.readline

k, s, n = input().split()
lst = [input().strip() for _ in range(int(n))]

height = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
width = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

rev_height = {v: k for k, v in height.items()}
rev_width = {v: k for k, v in width.items()}

move = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, 1),
    "T": (0, -1),
    "RT": (1, -1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (-1, 1)
}

k_l, k_r = k
s_l, s_r = s

king_x, king_y = width[k_l], height[k_r]
stone_x, stone_y = width[s_l], height[s_r]

for cmd in lst:
    dx, dy = move[cmd]

    nx, ny = king_x + dx, king_y + dy

    if not (0 <= nx < 8 and 0 <= ny < 8):
        continue

    if nx == stone_x and ny == stone_y:
        sx, sy = stone_x + dx, stone_y + dy

        if not (0 <= sx < 8 and 0 <= sy < 8):
            continue

        stone_x, stone_y = sx, sy

    king_x, king_y = nx, ny

print(rev_width[king_x] + rev_height[king_y])
print(rev_width[stone_x] + rev_height[stone_y])