import sys

input = sys.stdin.readline

n, c = map(int, input().split())

nums = list(map(int, input().split()))

message = dict()

for num in nums:
    if num not in message:
        message[num] = 1
    else:
        message[num] += 1

message = sorted(message.items(), key=lambda x: x[1], reverse=True)


for a, b in message:
    for _ in range(b):
        print(a, end=' ')