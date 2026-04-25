t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    
    answer = 0
    if n > 9 or k > 9:
        answer = -1
    else:
        answer = n * k
    print(f'#{i} {answer}')