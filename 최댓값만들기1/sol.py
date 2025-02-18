def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

def solution1(numbers):
    numbers.sort(reverse = True)
    return numbers[0] * numbers[1]

def solution2(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[i + 1]:
                numbers[j], numbers[i + 1] = numbers[i + 1], numbers[j]
    return numbers[-1] * numbers[-2]