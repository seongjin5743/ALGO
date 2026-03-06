a, b = map(int, input().split())

if a > b:
    a, b = b, a

print(max(0, b - a - 1))

for num in range(a + 1, b):
    print(num, end=' ')