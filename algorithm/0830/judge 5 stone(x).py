def check(table, N):
    count = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 'o':
                count += 1
                for k in range(j+1, N): # 가로 확인
                    if table[i][k] == 'o':
                        count += 1
                if count == 5:
                    return 'YES'
                count = 1
                for k in range(i+1, N): # 세로 확인
                    if table[k][j] == 'o':
                        count += 1
                if count == 5:
                    return 'YES'
                count = 0
                big_num = max(i, j)
                for k in range(N-big_num):
                    if table[i+k][j+k] == 'o':
                        count += 1
                if count == 5:
                    return 'YES'
                count = 0
                big_num = max(i, N-j-1)
                for k in range(N-big_num):
                    if table[i+k][j-k] == 'o':
                        count += 1
                if count == 5:
                    return 'YES'
    return 'NO'


T = int(input())
for tc in range(T):
    N = int(input())
    table = [list(input()) for _ in range(N)]
    ans = check(table, N)
    print(f'#{tc+1} {ans}')
