T = int(input())
for tc in range(T):
    word = input()
    sent = input()
    max_word = 0
    for i in range(len(word)):
        count_word = 0
        for j in range(len(sent)):
            if sent[j] == word[i]:
                count_word += 1
        if count_word > max_word:
            max_word = count_word
    print(f'#{tc+1} {max_word}')