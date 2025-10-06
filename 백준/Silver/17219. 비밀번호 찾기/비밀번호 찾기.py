import sys
input = sys.stdin.readline

n, m = map(int, input().split())

db = {}
for _ in range(n):
    site, password = input().split()
    db[site] = password.strip()

for _ in range(m):
    query = input().strip()
    print(db[query])