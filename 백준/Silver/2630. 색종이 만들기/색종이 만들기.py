n = int(input())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

w, b = 0, 0

def count_colors(x, y, size):
    global w, b
    color = maze[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if maze[i][j] != color:
                same = False
                break
        if not same:
            break
    
    if same:
        if color == 0:
            w += 1
        else:
            b += 1
        return
    
    new_size = size // 2
    count_colors(x, y, new_size)
    count_colors(x, y + new_size, new_size)
    count_colors(x + new_size, y, new_size)
    count_colors(x + new_size, y + new_size, new_size)

count_colors(0, 0, n)
print(w, b)