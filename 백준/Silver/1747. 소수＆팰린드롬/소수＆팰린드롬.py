def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def next_palindrome_prime(n):
    num = n
    while True:
        if str(num) == str(num)[::-1]:
            if is_prime(num):
                return num
        num += 1

n = int(input())
print(next_palindrome_prime(n))