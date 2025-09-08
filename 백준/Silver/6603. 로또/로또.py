while True:
    nums1 = list(map(int, input().split()))

    if nums1 == [0]:
        break

    k, s = nums1[0], nums1[1:]

    out = []

    def recur(num):
        if len(out) == 6:
            print(*out)
            return
        
        for i in range(num, k):
            out.append(s[i])
            recur(i + 1)
            out.pop()

    recur(0)
    print('')