n = int(input())

time = []

for _ in range(n):
    x, y = map(int, input().split())
    time.append((x, y))

time.sort(key= lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in time:
    if start >= end_time:
        end_time = end
        count += 1

print(count)