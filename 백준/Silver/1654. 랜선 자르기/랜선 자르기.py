import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lan = []

for _ in range(k):
    lan.append(int(input()))

lan.sort()

start = 1
end = lan[-1]

while start <= end:
    mid = (start + end) // 2
    count = sum(x // mid for x in lan)
    
    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)