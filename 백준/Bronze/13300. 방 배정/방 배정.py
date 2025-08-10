n, k = map(int, input().split())

graph = [[] for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split())
    graph[y - 1].append(s)

room = 0
for i in range(6):
    male = graph[i].count(1)
    female = graph[i].count(0)
    if male % k != 0:
        room += 1
    if female % k != 0:
        room += 1
    room += male // k
    room += female // k
print(room)