def min_produce(i, sumV):
    global minV
    if sumV >= minV:
        return
    if i == N:
        if minV >= sumV:
            minV = sumV
        return
    for j in range(N):
        if check[j] == 0:
            check[j] = 1
            min_produce(i + 1, sumV + V[i][j])
            check[j] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    minV = 100 * N
    check = [0] * N
    min_produce(0, 0)
    print(f'#{tc+1} {minV}')
