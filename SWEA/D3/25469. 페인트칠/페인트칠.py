T = int(input())

for t in range(1, T + 1):
    h, w = map(int, input().split())
    maze = [list(input().strip()) for _ in range(h)]
    h_count, w_count = 0, 0
    for y in range(h):
        if all(x == '#' for x in maze[y]):
            h_count += 1
    if h_count == h:
        print(min(h, w))
        continue
    for x in range(w):
        if all(maze[y][x] == '#' for y in range(h)):
            w_count += 1
    print(h_count + w_count)