import sys

input = sys.stdin.readline

n = int(input())

p = list(map(int, input().split()))

p.sort()

sum = 0
qwer = 0

for i in p:
    qwer += i
    sum += qwer

print(sum)