import sys
input = sys.stdin.readline

ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

answer = 0
if ca < cr:
    answer += cr - ca
if ba < br:
    answer += br - ba
if pa < pr:
    answer += pr - pa
print(answer)