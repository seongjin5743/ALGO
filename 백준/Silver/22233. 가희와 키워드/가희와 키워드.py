import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = set([input().strip() for _ in range(n)])

for _ in range(m) :
   key_set = set(input().strip().split(','))
   keywords -= key_set
   print(len(keywords))