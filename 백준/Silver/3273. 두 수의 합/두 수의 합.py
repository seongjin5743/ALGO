import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()

left = 0
right = n - 1

answer = 0

while left < right:
    if a[left] + a[right] == x:
        answer += 1
        left += 1
        right -= 1
    elif a[left] + a[right] < x:
        left += 1
    else:
        right -= 1

print(answer)