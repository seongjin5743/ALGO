def solution(want, number, discount):
    answer = 0
    fruits = []
    
    for w, n in zip(want, number):
        fruits.extend([w] * n)
    
    fruits.sort()
    
    for i in range(len(discount) - 9):
        qwer = discount[i:i+10]
        qwer.sort()
        if fruits == qwer:
            answer += 1
        
        
#     for i in range(len(discount) - 10):
#         flag = False
#         qwer = discount[i:i+10]
#         for j in range(len(want)):
#             if qwer.count(want[j]) >= number[j]:
#                 flag = True
#             else:
#                 flag = False

#         if flag:
#             answer += 1
            
    return answer