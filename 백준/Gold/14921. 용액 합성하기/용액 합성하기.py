import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
nums.sort()

start = 0
end = n - 1
ans = (0, 0)

min_num = int(1e9)

while start < end:
    total = nums[start] + nums[end]

    if abs(total) < min_num:
        min_num = abs(total)
        ans = (nums[start], nums[end])

    if total < 0:
        start += 1
    else:
        end -= 1
print(ans[0] + ans[1])