n = int(input())
maze = [input() for _ in range(n)]

def digit_sum(s):
    return sum(int(ch) for ch in s if ch.isdigit())

maze.sort(key=lambda x: (len(x), digit_sum(x), x))

for m in maze:
    print(m)