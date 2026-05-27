T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    white = [0] * N
    blue = [0] * N
    red = [0] * N

    for i in range(N):
        white[i] = M - arr[i].count('W')
        blue[i] = M - arr[i].count('B')
        red[i] = M - arr[i].count('R')

    answer = float('inf')

    for w in range(N - 2):
        for b in range(w + 1, N - 1):

            total = 0

            for i in range(0, w + 1):
                total += white[i]

            for i in range(w + 1, b + 1):
                total += blue[i]

            for i in range(b + 1, N):
                total += red[i]

            answer = min(answer, total)

    print(f'#{t} {answer}')