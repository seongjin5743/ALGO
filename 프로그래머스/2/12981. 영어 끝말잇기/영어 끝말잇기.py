def solution(n, words):
    word = []

    for i in range(len(words)):
        if words[i] in word:
            return [(i % n) + 1, (i // n) + 1]

        if i > 0 and words[i - 1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]

        word.append(words[i])

    return [0, 0]