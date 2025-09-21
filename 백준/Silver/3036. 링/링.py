import math

n = int(input())

rings = list(map(int, input().split()))

ring = rings[0]
for i in range(1, n):
    num = math.gcd(ring, rings[i])
    print(f'{ring // num}/{rings[i] // num}')