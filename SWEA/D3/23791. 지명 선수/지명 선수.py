T = int(input())

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    visited = [False] * (n + 1)
    answer = ['O'] * (n + 1)

    i = j = 0
    picked = 0
    turn = 0

    while picked < n:
        if turn % 2 == 0:  # A팀
            while visited[A[i]]:
                i += 1
            player = A[i]
            visited[player] = True
            answer[player] = 'A'
            i += 1
        else:  # B팀
            while visited[B[j]]:
                j += 1
            player = B[j]
            visited[player] = True
            answer[player] = 'B'
            j += 1

        picked += 1
        turn += 1

    print(''.join(answer[1:]))