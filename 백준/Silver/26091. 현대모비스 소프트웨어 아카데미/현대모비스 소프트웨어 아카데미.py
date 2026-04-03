import sys
input = sys.stdin.readline

n, m = map(int, input().split())

member = list(map(int, input().split()))
member.sort()

left, right = 0, n - 1

answer = 0
while left < right:
    if member[left] + member[right] >= m:
        answer += 1
        left += 1
        right -= 1
    else:
        left += 1

print(answer)