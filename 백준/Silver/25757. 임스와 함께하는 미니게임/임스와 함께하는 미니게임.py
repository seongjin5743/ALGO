n, game = input().split()
n = int(n)

players = set()

for _ in range(n):
    players.add(input())

games = {'Y': 1, 'F': 2, 'O': 3}

print(len(players) // games[game])