T = int(input())

for t in range(1, T + 1):
    num = list(input().strip())

    if num.count('x') <= 7:
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'#{t} {answer}')