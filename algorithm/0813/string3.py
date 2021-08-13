for tc in range(10):
    T = int(input())
    word = input()
    sent = input()
    count = 0
    for i in range(len(sent)-1):
        if sent[i] == word[0]:
            check = 1
            for j in range(1, len(word)):
                if sent[i+j] == word[j]:
                    check += 1
            if check == len(word):
                count += 1
    print(f'#{T} {count}')
