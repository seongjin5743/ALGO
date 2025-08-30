words = input()

sentence = words + words

min_num = 1000

for i in range(len(words)):
    min_num = min(min_num, sentence[i:i+words.count('a')].count('b'))

print(min_num)