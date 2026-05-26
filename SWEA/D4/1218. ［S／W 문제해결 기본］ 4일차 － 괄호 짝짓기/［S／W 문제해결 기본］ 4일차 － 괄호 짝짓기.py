for t in range(1, 11):
    T = int(input())
    N = input()

    stack = []
    ans = 1

    pair = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    for ch in N:
        if ch in "([{<":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                ans = 0
                break

            stack.pop()

    if stack:
        ans = 0

    print(f"#{t} {ans}")