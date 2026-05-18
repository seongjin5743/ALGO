T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    possible = set()
    possible.add(0)

    for score in scores:
        new_scores = set()

        for s in possible:
            new_scores.add(s + score)

        possible.update(new_scores)

    print(f"#{tc} {len(possible)}")