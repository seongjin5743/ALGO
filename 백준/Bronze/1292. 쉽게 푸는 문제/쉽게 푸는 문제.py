result = []

for i in range(1, 46):
    result += i * [i]

a, b = map(int, input().split())

print(sum(result[a - 1:b]))