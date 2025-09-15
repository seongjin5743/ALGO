n = int(input())

j = 2
while True:
    if n == 1:
        break

    if n % j == 0:
        n /= j
        print(j)
    else:
        j += 1