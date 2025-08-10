s1 = input().strip()
s2 = input().strip()

cnt = [0] * 26

for ch in s1:
    cnt[ord(ch) - ord('a')] += 1
for ch in s2:
    cnt[ord(ch) - ord('a')] -= 1

print(sum(abs(x) for x in cnt))