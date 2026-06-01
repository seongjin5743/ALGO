import math

def solution(arrayA, arrayB):
    gA = math.gcd(*arrayA)
    gB = math.gcd(*arrayB)

    answer = 0

    if all(b % gA != 0 for b in arrayB):
        answer = max(answer, gA)

    if all(a % gB != 0 for a in arrayA):
        answer = max(answer, gB)

    return answer