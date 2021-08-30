T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    for i in range(N):  # + 모양
        for j in range(N):
            kill = 0
            for k in range(-M+1, M):
                if 0 <= i + k < N:
                    kill += flies[i+k][j]
            for k in range(-M+1, M):
                if 0 <= j + k < N:
                    kill += flies[i][j+k]
            kill -= flies[i][j]
            if max_kill < kill:
                max_kill = kill

    for i in range(N):  # x 모양
        for j in range(N):
            kill = 0
            for k in range(-M+1, M):
                if 0 <= i + k < N and 0 <= j + k < N:
                    kill += flies[i+k][j+k]
            for k in range(-M+1, M):
                if 0 <= i + k < N and 0 <= j - k < N:
                    kill += flies[i+k][j-k]
            kill -= flies[i][j]
            if max_kill < kill:
                max_kill = kill
    print(f'#{tc+1} {max_kill}')
