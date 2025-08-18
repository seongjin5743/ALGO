p = int(input())

heights_list = [list(map(int, input().split())) for _ in range(p)]

for heights in heights_list:
    one = heights[0]
    height_line = heights[1:]
    answer = 0
    line = []

    for h in height_line:
        cnt = 0
        for prev in line:
            if prev > h:
                cnt += 1
        answer += cnt
        line.append(h)

    print(one, answer)