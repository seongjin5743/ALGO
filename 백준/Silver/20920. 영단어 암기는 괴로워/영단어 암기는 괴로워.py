from collections import Counter
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

words = []
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words.append(word)

counter = Counter(words)

sorted_words = sorted(counter.keys(), key= lambda x: (-counter[x], -len(x), x))

for word in sorted_words:
    print(word)