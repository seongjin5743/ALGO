for t in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split('+')))
    print(f"#{t} {sum(lst)}")