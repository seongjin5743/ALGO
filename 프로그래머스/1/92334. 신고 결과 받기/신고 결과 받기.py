def solution(id_list, report, k):
    reported_list = {user_id : 0 for user_id in id_list}
    answer = [0] * len(id_list)

    unique_report = set(report)
    for report in unique_report:
        user, reported_user = report.split()
        reported_list[reported_user] += 1

    for report in unique_report:
        user, reported_user = report.split()
        if reported_list[reported_user] >= k:
            answer[id_list.index(user)] += 1

    return answer