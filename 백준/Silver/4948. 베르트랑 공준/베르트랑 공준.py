import sys

input = sys.stdin.readline

m = 246912
prime = [True] * (m + 1)
prime[0] = prime[1] = False    

for i in range(2, int(m ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, m + 1, i):
            prime[j] = False

while True:
    n = int(input())
    
    if n == 0:
        break
    
    print(sum(prime[n + 1: 2 * n + 1]))