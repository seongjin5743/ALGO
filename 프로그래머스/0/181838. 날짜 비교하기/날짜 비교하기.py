def solution(date1, date2):
    date1 = int(str(date1[0]) + str(date1[1]) + str(date1[2]))
    date2 = int(str(date2[0]) + str(date2[1]) + str(date2[2]))
    return 1 if date1 < date2 else 0