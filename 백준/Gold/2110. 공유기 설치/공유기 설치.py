n, c = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()

left = 1
right = lst[-1] - lst[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    cur = lst[0]
    count = 1

    for i in range(1, n):
        if lst[i] >= cur + mid:
            count += 1
            cur = lst[i]

    if count >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)