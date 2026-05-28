def solution(record):
    answer = []

    nickname = {}
    logs = []

    for r in record:
        temp = r.split()

        command = temp[0]
        uid = temp[1]

        if command == 'Enter':
            nickname[uid] = temp[2]
            logs.append((uid, 'Enter'))

        elif command == 'Leave':
            logs.append((uid, 'Leave'))

        else:
            nickname[uid] = temp[2]

    for uid, command in logs:
        if command == 'Enter':
            answer.append(f'{nickname[uid]}님이 들어왔습니다.')
        else:
            answer.append(f'{nickname[uid]}님이 나갔습니다.')

    return answer