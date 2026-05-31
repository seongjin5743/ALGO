def solution(genres, plays):
    answer = []

    score = {}

    for i in range(len(genres)):
        if genres[i] not in score:
            score[genres[i]] = []

        score[genres[i]].append((plays[i], i))

    total = {}

    for x in score:
        total[x] = sum(num for num, idx in score[x])

    total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in total:
        score[genre].sort(key=lambda x: (-x[0], x[1]))

        for i in range(min(2, len(score[genre]))):
            answer.append(score[genre][i][1])

    return answer