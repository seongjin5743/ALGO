def solution(id_pw, db):
    target_id, target_pw = id_pw
    for db_id, db_pw in db:
        if db_id == target_id:
            if db_pw == target_pw:
                return 'login'
            else:
                return 'wrong pw'
                
    return 'fail'