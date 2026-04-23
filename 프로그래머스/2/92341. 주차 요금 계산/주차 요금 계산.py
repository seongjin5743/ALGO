def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    
    in_dict = {}
    total_time = {}
    
    for record in records:
        time, num, inout = record.split()
        h, m = map(int, time.split(':'))
        time = h * 60 + m
        
        if inout == 'IN':
            in_dict[num] = time
        else:
            duration = time - in_dict[num]
            
            if num in total_time:
                total_time[num] += duration
            else:
                total_time[num] = duration
            
            del in_dict[num]
    
    for num in in_dict:
        duration = 1439 - in_dict[num]
        
        if num in total_time:
            total_time[num] += duration
        else:
            total_time[num] = duration
    
    answer = []
    for num in sorted(total_time):
        t = total_time[num]
        
        if t <= base_time:
            fee = base_fee
        else:
            extra = t - base_time
            fee = base_fee + ((extra + unit_time - 1) // unit_time) * unit_fee
        
        answer.append(fee)
    
    return answer