def re_check(word_list, N):
    for i in range(N-1):
        if word_list[i] == word_list[i+1]:
            word_list.pop(i)
            word_list.pop(i)
            return re_check(word_list, len(word_list))
            break
    return len(word_list)

T = int(input())
for tc in range(T):
    word = input()
    word_list = []
    for i in range(len(word)):
        word_list.append(word[i])
    N = len(word_list)
    ans = re_check(word_list, N)
    print(f'#{tc+1} {ans}')

