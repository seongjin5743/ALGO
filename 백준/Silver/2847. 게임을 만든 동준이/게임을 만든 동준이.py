n = int(input())

maze = []
for _ in range(n):
    maze.append(int(input()))

max_num = maze[-1]

answer = 0
for i in range(n - 2, -1, -1):
    if max_num <= maze[i]:
        num = maze[i] - max_num + 1
        answer += num
        max_num -= 1
    else:
        max_num = maze[i]

print(answer)