import sys

input = sys.stdin.readline

t = int(input())

m = 1000000
prime = [True] * (m + 1)
prime[0], prime[1] = False, False

for i in range(2, int(m ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, m + 1, i):
            prime[j] = False

for _ in range(t):
    n = int(input())
    for i in range(n // 2, 1, -1):
        if prime[i] and prime[n - i]:
            print(i, n - i)
            break