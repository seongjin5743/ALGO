n = int(input())
k = int(input())

sensors = list(map(int, input().split()))

sensors.sort()

s = []

for i in range(n - 1):
    s.append(sensors[i + 1] - sensors[i])

s.sort(reverse=True)

print(sum(s[k-1:]))