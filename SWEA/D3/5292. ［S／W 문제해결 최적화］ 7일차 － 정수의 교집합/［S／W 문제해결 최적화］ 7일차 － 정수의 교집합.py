T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    answer = len(set(A + B))
    print(f"#{t} {n + m - answer}")