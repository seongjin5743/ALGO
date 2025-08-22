n, game = input().split()
n = int(n)

players = set(input() for _ in range(n))
games = {'Y': 1, 'F': 2, 'O': 3}

print(len(players) // games[game])