T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
    for k in range(1, M+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if M % k == 0:
                    if table[i-1][j-1] == 0:
                        table[i-1][j-1] = 1
                    else:
                        table[i-1][j-1] = 0
                elif (i + j) % k == 0:
                    if table[i-1][j-1] == 0:
                        table[i-1][j-1] = 1
                    else:
                        table[i-1][j-1] = 0
    count = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                count += 1
    print(f'#{tc+1} {count}')

