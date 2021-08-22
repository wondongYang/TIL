def vert(words_list, word):
    if len(words_list) > 0:
        count = []
        for i in range(len(words_list)):
            word += words_list[i][0]
            words_list[i].pop(0)
        for i in range(len(words_list)):
            if len(words_list[i]) == 0:
                count.append(i)
        for i in range(len(count)):
            words_list.pop(count[i]-i)
        return vert(words_list, word)
    else:
        return word


T = int(input())
for tc in range(T):
    words = [list(input()) for _ in range(5)]
    word = ''
    ans = vert(words, word)
    print(f'#{tc+1} {ans}')

