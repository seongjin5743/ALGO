import math

def solution(signals):
    answer = -1
    
    total = signals[0][0] + signals[0][1] + signals[0][2]
    
    for i in range(1, len(signals)):
        cycle = signals[i][0] + signals[i][1] + signals[i][2]
        total = total * cycle // math.gcd(total, cycle)
    
    for t in range(1, total + 1):
        check = True
        
        for i in range(len(signals)):
            G = signals[i][0]
            Y = signals[i][1]
            R = signals[i][2]
            
            cycle = G + Y + R
            time = (t - 1) % cycle
            
            if not (G <= time < G + Y):
                check = False
                break
        
        if check:
            answer = t
            break
    
    return answer