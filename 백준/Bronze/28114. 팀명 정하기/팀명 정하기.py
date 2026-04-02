import sys
input = sys.stdin.readline

stu = []

for _ in range(3):
    p, y, s = input().split()
    stu.append((int(p), int(y), s))

stu.sort(key=lambda x: x[1])

team1 = ''

for p, y, s in stu:
    team1 += str(y % 100)

team2 = ''

stu.sort(key=lambda x: -x[0])

for p, y, s in stu:
    team2 += s[0]

print(team1)
print(team2)