T = int(input())

for t in range(1, T + 1):
    num = input().strip()
    middle = len(num) // 2
    answer = 0

    if len(num) % 2 == 0:
        answer = int(num[:middle]) + int(num[middle:])
    else:
        a1 = int(num[:middle]) + int(num[middle:])
        a2 = int(num[:middle + 1]) + int(num[middle + 1:])
        answer = min(a1, a2)

    print(f'#{t} {answer}')