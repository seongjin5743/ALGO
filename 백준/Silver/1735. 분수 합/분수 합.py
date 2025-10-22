import math
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

num2 = math.lcm(b, m)

num1 = (num2 // b) * a + (num2 // m) * n

answer = math.gcd(num1, num2)

print(num1 // answer, num2 // answer)