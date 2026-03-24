def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    
    time = 0
    combo = 0
    
    for attack_time, damage in attacks:
        while time < attack_time - 1:
            time += 1
            combo += 1
            
            health = min(max_health, health + x)
            
            if combo == t:
                health = min(max_health, health + y)
                combo = 0
                
        time = attack_time
        health -= damage
        combo = 0
        
        if health <= 0:
            return -1
    
    return health