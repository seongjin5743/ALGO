n = int(input())

people = []
for _ in range(n):
    people.append(list(map(int, input().split())))

answer = []
for kg, cm in people:
    rank = 1
    for kg1, cm1 in people:
        if kg < kg1 and cm < cm1:
            rank += 1
    answer.append(rank)
print(*answer)