T = int(input())
for tc in range(T):
    N = int(input())
    Colors = [list(map(int, input().split())) for _ in range(N)]
    list_N = [[(0, 0)] * ((Colors[i][2] - Colors[i][0] + 1) * (Colors[i][3] - Colors[i][1] + 1)) for i in range(N)]
    list_sum = []
    list_ans = []
    for i in range(N):
        a = 0
        for k in range(Colors[i][0], Colors[i][2] + 1):
            for t in range(Colors[i][1], Colors[i][3] + 1):
                list_N[i][a] = (k, t)
                a += 1
        list_sum += list_N[i]
    for i in list_sum:
        if i not in list_ans:
            list_ans.append(i)
    ans = len(list_sum) - len(list_ans)
    print(f'#{tc+1} {ans}')

# 색 관련 수정x 더 고민해보기
