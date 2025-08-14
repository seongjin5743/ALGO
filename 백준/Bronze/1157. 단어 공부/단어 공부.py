alpha = input()

alphabet = {}

for al in alpha:
    al = al.upper()
    if al not in alphabet:
        alphabet[al] = 1
    else:
        alphabet[al] += 1
answer = [alp for alp, num in alphabet.items() if max(alphabet.values()) == num]
if len(answer) == 1:
    print(*answer)
else:
    print('?')