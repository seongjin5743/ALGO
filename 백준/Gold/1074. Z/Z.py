n, r, c = map(int, input().split())

answer = 0

while True:
    if n == 0:
        break

    n -= 1

    if r < 2 ** n and c < 2 ** n:
        answer += (2 ** n) * (2 ** n) * 0
    elif r < 2 ** n and c >= 2 ** n:
        answer += (2 ** n) * (2 ** n) * 1
        c -= 2 ** n
    elif r >= 2 ** n and c < 2 ** n:
        answer += (2 ** n) * (2 ** n) * 2
        r -= 2 ** n
    elif r >= 2 ** n and c >= 2 ** n:
        answer += (2 ** n) * (2 ** n) * 3
        r -= 2 ** n
        c -= 2 ** n
print(answer)