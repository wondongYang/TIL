di, dj = [0, 1], [1, 0]

def f(i, j, sumV):
    global minV
    if i == N - 1 and j == N - 1:   # 도착
        if minV > sumV:
            minV = sumV
            return
    else:
        if sumV >= minV:    # sum이 더 크면 더이상 계산x
            return
        else:
            for k in range(2):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    f(ni, nj, sumV + arr[ni][nj])

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 2 * 10 * N - 10
    f(0, 0, arr[0][0])
    print(f'#{tc+1} {minV}')
