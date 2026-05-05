T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    def binary_search(x):
        left, right = 0, n - 1
        check = 0

        while left <= right:
            mid = (left + right) // 2

            if A[mid] == x:
                return 1

            elif A[mid] > x:
                if check == 1:
                    break
                check = 1
                right = mid - 1

            else:
                if check == 2:
                    break
                check = 2
                left = mid + 1

        return 0

    answer = 0
    for num in B:
        answer += binary_search(num)

    print(f"#{t} {answer}")