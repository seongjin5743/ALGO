T = int(input())

for t in range(1, T + 1):
    n = int(input())
    S = list(map(int, input().split()))
    
    total = sum(S)
    
    if total % n == 0:
        print(f"#{t} {total // n}")
    else:
        print(f"#{t} {total / n}")