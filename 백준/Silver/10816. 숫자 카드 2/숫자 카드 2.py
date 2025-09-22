import bisect

def cnt(arr, target):
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    return right - left

n = int(input())
num1 = list(map(int, input().split()))
m = int(input())
num2 = list(map(int, input().split()))

answer = []

num1.sort()

for num in num2:
    answer.append(cnt(num1, num))

print(*answer)