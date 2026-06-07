def time_to_minute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    time_dict = {}
    
    for start, end in book_time:
        start_min = time_to_minute(start)

        end_min = time_to_minute(end) + 10 
        
        for i in range(start_min, end_min):
            if i in time_dict:
                time_dict[i] += 1
            else:
                time_dict[i] = 1

    return max(time_dict.values())