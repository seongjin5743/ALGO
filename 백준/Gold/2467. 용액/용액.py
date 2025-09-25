n = int(input())

liq = list(map(int, input().split()))

left = 0
right = n - 1

ans = abs(liq[left] + liq[right])
ans_left = left
ans_right = right

while left < right:
    temp = liq[left] + liq[right]

    if abs(temp) < ans:
        ans_left = left
        ans_right = right
        ans = abs(temp)
        if ans == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -=1

print(liq[ans_left], liq[ans_right])