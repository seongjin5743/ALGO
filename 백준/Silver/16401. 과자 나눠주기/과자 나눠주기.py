import sys

input = sys.stdin.readline

m, n = map(int, input().split())

snack = list(map(int, input().split()))

start = 1
end = max(snack)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(x // mid for x in snack)
    
    if count < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1
print(result)