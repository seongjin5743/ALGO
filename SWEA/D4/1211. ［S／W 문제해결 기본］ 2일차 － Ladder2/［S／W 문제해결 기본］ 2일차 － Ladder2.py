for t in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    min_count = float('inf')

    for start_x in range(100):

        if ladder[0][start_x] != 1:
            continue

        x, y = start_x, 0
        count = 0

        visited = [[False] * 100 for _ in range(100)]
        visited[y][x] = True

        while y < 99:

            if x - 1 >= 0 and ladder[y][x - 1] == 1 and not visited[y][x - 1]:

                while x - 1 >= 0 and ladder[y][x - 1] == 1:
                    x -= 1
                    count += 1
                    visited[y][x] = True
            elif x + 1 < 100 and ladder[y][x + 1] == 1 and not visited[y][x + 1]:

                while x + 1 < 100 and ladder[y][x + 1] == 1:
                    x += 1
                    count += 1
                    visited[y][x] = True

            y += 1
            count += 1
            visited[y][x] = True

        if count <= min_count:
            min_count = count
            answer = start_x

    print(f"#{t} {answer}")