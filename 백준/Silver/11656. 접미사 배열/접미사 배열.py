import sys

input = sys.stdin.readline

s = input().strip()

mess = []

for i in range(len(s)):
    mess.append(s[i:])

mess.sort()

for m in mess:
    print(m)