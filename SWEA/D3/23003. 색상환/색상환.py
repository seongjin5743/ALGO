t = int(input())

color = [input().split() for _ in range(t)]

color_map = {
    'red': 0,
    'orange': 1,
    'yellow': 2,
    'green': 3,
    'blue': 4,
    'purple': 5
}

for c1, c2 in color:
    if c1 == c2:
        print('E')
    else:
        num = abs(color_map[c1] - color_map[c2])

        if num == 1 or num == 5:
            print('A')
        elif num == 3:
            print('C')
        else:
            print('X')