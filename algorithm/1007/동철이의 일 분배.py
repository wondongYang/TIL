def max_p(i, crossV):
    global maxV
    if crossV <= maxV:
        return
    if i == N:
        if maxV <= crossV:
            maxV = crossV
        return
    for j in range(N):
        if check[j] == 0:
            check[j] = 1
            max_p(i + 1, crossV * P[i][j])
            check[j] = 0
            
T = int(input())
for tc in range(T):
    N = int(input())
    P_100 = [list(map(int, input().split())) for _ in range(N)]
    P = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            P[i][j] = P_100[i][j] / 100
    maxV = 0
    check = [0] * N
    max_p(0, 1)
    print(f'#{tc+1} {maxV * 100:.6f}')