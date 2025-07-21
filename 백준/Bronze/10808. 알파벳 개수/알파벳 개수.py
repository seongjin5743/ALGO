words = input()

result = [0] * 26

for word in words:
    result[ord(word) - 97] += 1

print(*result)