n, s = map(int, input().split())

nums = list(map(int, input().split()))

p = [0]

val = 0
for i in range(n):
    val += nums[i]
    p.append(val)

answer = n + 1
start, end = 0, 1

while start < n + 1 and end < n + 1:
    if p[end] - p[start] >= s:
        answer = min(answer, end - start)
        start += 1
    else:
        end += 1

print(0 if answer == n + 1 else answer)