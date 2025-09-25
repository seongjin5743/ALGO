import sys

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()

answer = []
for ml in mlist:
    left, right = 0, n - 1
    found = False

    while left <= right:
        mid = (left + right) // 2
        if nlist[mid] == ml:
            answer.append(1)
            found = True
            break
        elif nlist[mid] < ml:
            left = mid + 1
        else:
            right = mid - 1
    if not found:
        answer.append(0)

print(*answer)