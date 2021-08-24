def f(i, arr, n, sum):
    global min_sum
    if i == n:
        if min_sum > sum:
            min_sum = sum
    else:
        for j in range(i, n):
            for k in range(n):
                arr[k][i], arr[k][j] = arr[k][j], arr[k][i]
            f(i+1, arr, n, sum + arr[i][i])
            for k in range(n):
                arr[k][i], arr[k][j] = arr[k][j], arr[k][i]

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s = []
    min_sum = 10 * N
    f(0, arr, N, 0)
    print(f'#{tc+1} {min_sum}')


