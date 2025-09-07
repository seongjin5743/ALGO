from itertools import combinations

n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort()

for comb in combinations(data, m):
    print(*comb)