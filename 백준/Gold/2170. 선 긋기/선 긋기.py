import sys

input = sys.stdin.readline

n = int(input())

dots = []

for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))

dots.sort()

answer = 0

m_x, m_y = dots[0]

for x, y in dots[1:]:
    if x <= m_y:
        m_y = max(m_y, y)
    else:
        answer += m_y - m_x
        m_x, m_y = x, y

answer += m_y - m_x

print(answer)