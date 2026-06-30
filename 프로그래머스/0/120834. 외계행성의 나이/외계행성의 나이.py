def solution(age):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    age = str(age)
    
    for i in age:
        answer += alpha[int(i)]
        
    return answer