h, w = map(int, input().split())
block = list(map(int, input().split()))

answer = 0

for i in range(1, w-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])
    answer += max(0, min(left_max, right_max) - block[i])

print(answer)