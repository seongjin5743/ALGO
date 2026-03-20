def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(t):
        m, s = map(int, t.split(':'))
        return m * 60 + s
    
    def to_time(sec):
        return f"{sec // 60:02d}:{sec % 60:02d}"
    
    video = to_sec(video_len)
    cur = to_sec(pos)
    op_s = to_sec(op_start)
    op_e = to_sec(op_end)

    if op_s <= cur <= op_e:
        cur = op_e
    
    for command in commands:
        if command == "prev":
            cur = max(0, cur - 10)
        else:
            cur = min(video, cur + 10)

        if op_s <= cur <= op_e:
            cur = op_e
    
    return to_time(cur)