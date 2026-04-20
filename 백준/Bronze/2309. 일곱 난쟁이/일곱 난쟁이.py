import sys
from itertools import combinations

input = sys.stdin.readline

shorts = [int(input()) for _ in range(9)]
shorts.sort()
seven = tuple(combinations(shorts, 7))

for s in seven:
    if sum(s) == 100:
        
        for i in s:
            print(i)
        break