T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 가로 체크
    for i in range(N):
        count_list = []
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count += 1
            else:
                count = 0
            count_list.append(count)
        count_list.append(0)
        for k in range(N):
            if count_list[k] == K and count_list[k+1] == 0:
                ans += 1

    # 세로 체크
    for i in range(N):
        count_list = []
        count = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                count += 1
            else:
                count = 0
            count_list.append(count)
        count_list.append(0)
        for k in range(N):
            if count_list[k] == K and count_list[k + 1] == 0:
                ans += 1

    print(f'#{tc+1} {ans}')

