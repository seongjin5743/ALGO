n = int(input())

maze = list(set(input() for _ in range(n)))

maze.sort(key= lambda x: (len(x), x))

for m in maze:
    print(m)