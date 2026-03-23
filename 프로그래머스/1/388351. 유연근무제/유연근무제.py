def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        start = schedules[i]
        
        h = start // 100
        m = start % 100
        limit = h * 60 + m + 10
        
        ok = True
        
        for d in range(7):
            day = (startday + d) % 7
            
            if day in (6, 0):
                continue
            
            t = timelogs[i][d]
            th = t // 100
            tm = t % 100
            
            if th * 60 + tm > limit:
                ok = False
                break
        
        if ok:
            answer += 1
    
    return answer