import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    count = 0

    b_n = len(b)

    for i in a:
        start = 0
        end = b_n - 1

        while start <= end:
            mid = (start + end) // 2
            if b[mid] < i:
                start = mid + 1
            else:
                end = mid - 1
        count += start

    print(count)