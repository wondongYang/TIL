T = int(input())
for tc in range(T):
    word = input()
    sent = input()
    count = 0
    for i in range(len(sent)-len(word)+1):
        if sent[i] == word[0]:
            check = 1
            for j in range(1, len(word)):
                if sent[i+j] == word[j]:
                    check += 1
            if check == len(word):
                count += 1
    print(f'#{tc+1} {count}')