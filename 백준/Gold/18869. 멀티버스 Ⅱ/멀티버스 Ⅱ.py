import sys
input = sys.stdin.readline

n, m = map(int, input().split())

universes = []

for _ in range(n):
    arr = list(map(int, input().split()))
    
    sorted_arr = sorted(set(arr))
    rank = {v:i for i, v in enumerate(sorted_arr)}
    
    qwer = tuple(rank[x] for x in arr)
    universes.append(qwer)

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if universes[i] == universes[j]:
            count += 1

print(count)