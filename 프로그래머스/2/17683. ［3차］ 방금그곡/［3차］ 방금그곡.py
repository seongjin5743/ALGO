def solution(m, musicinfos):
    answer = []
    
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for info in musicinfos:
        start, end, name, melody = info.split(',')
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))

        duration = (eh * 60 + em) - (sh * 60 + sm)
        
        melody = melody.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        
        if duration < len(melody):
            melody = melody[0:duration]
        else:
            melody = (melody * ((duration // len(melody)) + 1))[0:duration]
        
        if m in melody:
            answer.append((name, duration))
            
    answer.sort(key=lambda x: x[1], reverse=True)
    
    if not answer:
        return "(None)"
    
    return answer[0][0]