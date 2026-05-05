T = int(input())

for t in range(1, T + 1):
    n = int(input())
    S = list(map(int, input().split()))
    answer = sum(S) / n
    
    if answer == sum(S) // n:
        print(f"#{t} {sum(S) // n}")
    else:
        print(f"#{t} {answer}")