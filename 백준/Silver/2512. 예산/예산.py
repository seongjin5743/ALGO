n = int(input())

nums = list(map(int, input().split()))

m = int(input())

low, high = 0, max(nums)

answer = 0

while low <= high:
    mid = (low + high) // 2
    total = sum(min(mid, num) for num in nums)

    if total <= m:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
print(answer)