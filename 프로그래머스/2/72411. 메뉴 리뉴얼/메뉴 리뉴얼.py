from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    counter = Counter()
    for order in orders:
        order = sorted(list(order))
        num = len(order)
        for i in range(2, num + 1):
            for combi in combinations(order, i):
                temp = ''.join(combi)
                counter[temp] += 1
    for num in course:
        max_value = 0

        for key, value in counter.items():
            if len(key) == num:
                if value > max_value:
                    max_value = value

        if max_value < 2:
            continue

        for key, value in counter.items():
            if len(key) == num and value == max_value:
                answer.append(key)
    return sorted(answer)