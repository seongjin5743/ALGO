import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

answer = 0

for i in range(n):
    target = a[i]
    left, right = 0, n - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        goal = a[left] + a[right]

        if goal == target:
            answer += 1
            break
        elif goal < target:
            left += 1
        else:
            right -= 1

print(answer)