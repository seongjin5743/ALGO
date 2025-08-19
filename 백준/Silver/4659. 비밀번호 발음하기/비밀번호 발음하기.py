vowels = "aeiou"

def is_valid(word):
    cnt_vowel, cnt_consonant = 0, 0

    for ch in word:
        if ch in vowels:
            cnt_vowel += 1
            cnt_consonant = 0
        else:
            cnt_consonant += 1
            cnt_vowel = 0

        if cnt_vowel == 3 or cnt_consonant == 3:
            return False
    
    return True

while True:

    word = input()

    if word == 'end':
        break
    
    answer1 = any(ch in vowels for ch in word)

    answer2 = is_valid(word)
            
    now_word = ''
    answer3 = True
    for i in range(len(word)):
        if now_word == word[i] and (now_word != 'e' and now_word != 'o'):
            answer3 = False
            break
        now_word = word[i]
    
    if answer1 and answer2 and answer3:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')