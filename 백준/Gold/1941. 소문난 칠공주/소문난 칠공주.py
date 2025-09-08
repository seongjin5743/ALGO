from collections import deque

maze = [list(input().strip()) for _ in range(5)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

stu = []
count = 0

def is_connected(students):
    visited = [[False] * 5 for _ in range(5)]
    queue = deque([students[0]])
    visited[students[0][0]][students[0][1]] = True
    students_set = set(students)

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if (ny, nx) in students_set and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

    for y, x in students:
        if not visited[y][x]:
            return False
    return True

def recur(idx, s_cnt, y_cnt):
    global count
    if len(stu) == 7:
        if s_cnt >= 4 and is_connected(stu):
            count += 1
        return

    for i in range(idx, 25):
        y, x = i // 5, i % 5
        stu.append((y, x))
        if maze[y][x] == 'S':
            recur(i + 1, s_cnt + 1, y_cnt)
        else:
            recur(i + 1, s_cnt, y_cnt + 1)
        stu.pop()

recur(0, 0, 0)
print(count)