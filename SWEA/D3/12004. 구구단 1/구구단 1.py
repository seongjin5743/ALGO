T = int(input())

for t in range(1, T + 1):
    n = int(input())
    answer = 'No'
    for x in range(1, 10):
        for y in range(1, 10):
            if x * y == n:
                answer = 'Yes'
    print(f'#{t} {answer}')