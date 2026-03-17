import sys

input = sys.stdin.readline

n = int(input())

roof = [int(input()) for _ in range(n)]
stack = []
sum = 0

for i in range(n):
    while stack and stack[-1] <= roof[i]:
        stack.pop()
    
    stack.append(roof[i])
    sum += len(stack) - 1

print(sum)