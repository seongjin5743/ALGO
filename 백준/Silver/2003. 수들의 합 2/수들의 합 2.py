n, m = map(int, input().split())
a = list(map(int, input().split()))

answer = 0
left = 0
right = 0
current_sum = 0

while True:
    if current_sum >= m:
        if current_sum == m:
            answer += 1
        current_sum -= a[left]
        left += 1
    elif right == n:
        break
    else:
        current_sum += a[right]
        right += 1

print(answer)