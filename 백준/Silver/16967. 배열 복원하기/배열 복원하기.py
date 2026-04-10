import sys
input = sys.stdin.readline

H, W, Y, X = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H + Y)]

A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        A[i][j] = B[i][j]
        if i >= Y and j >= X:
            A[i][j] -= A[i - Y][j - X]

for row in A:
    print(*row)