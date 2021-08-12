T = int(input())
for tc in range(T):
    N = int(input())
    Numbers = [list(map(int, input().split())) for _ in range(N)]
    sum_list = [[0] * N for _ in range(N)]
    ans_list = []
    for i in range(N):
        for j in range(N):
            sum_list[i][j] = sum(Numbers[i])
    for i in range(N):
        sub_list = Numbers.pop(i)
        for k in range(N):
            for j in range(N-1):
                sum_list[i][k] += Numbers[j][k]
        Numbers.insert(i, sub_list)
    for i in range(N):
        ans_list += sum_list[i]
    print(f'#{tc+1} {max(ans_list)}')