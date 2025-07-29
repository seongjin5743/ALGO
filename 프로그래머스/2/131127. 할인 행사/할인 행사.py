from collections import Counter

def solution(want, number, discount):
    answer = 0
    fruits = []
    
    for w, n in zip(want, number):
        fruits.extend([w] * n)
        
    for i in range(len(discount) - 9):
        qwer = discount[i:i+10]
        if Counter(fruits) == Counter(qwer):
            answer += 1
    return answer