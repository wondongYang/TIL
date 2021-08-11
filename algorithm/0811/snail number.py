T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(T):
    N = int(input())
    cnt = 1
    i, j, = 0, -1
    k = 0
    list_N = [[0] * N for _ in range(N)]
    while cnt <= N * N:
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and list_N[ni][nj] == 0:
            list_N[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k+1) % 4
    print(f'#{tc+1}')
    for i in list_N:
        print(" ".join(map(str, i)))