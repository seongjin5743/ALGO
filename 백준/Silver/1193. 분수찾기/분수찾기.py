n = int(input())

line = 0
total = 0

while total < n:
    line += 1
    total += line

pos = n - (total - line)

if line % 2 == 0:
    numerator = pos
    denominator = line - pos + 1
else:
    numerator = line - pos + 1
    denominator = pos

print(f"{numerator}/{denominator}")