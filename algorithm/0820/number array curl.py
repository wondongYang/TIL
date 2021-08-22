T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    ans_list = [[] for _ in range(N)]

    # 90, 180, 270도 돌린 리스트 3개 만들기
    for i in range(N):
        for j in range(N):
            ans_list[0].append(arr[N-j-1][i])
            ans_list[1].append(arr[N-i-1][N-j-1])
            ans_list[2].append(arr[j][N-i-1])

    # 리스트에서 숫자 출력하기
    print(f'#{tc+1}')
    for k in range(N):
        for i in range(3):
            for j in range(N**2):
                if j // N == k:
                    print(ans_list[i][j], end='')
            print('', end=' ')
        print()
