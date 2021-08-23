T = int(input())
for tc in range(T):
    N_M = list(map(int, input().split()))
    N = N_M[0]
    M = N_M[1]
    V = list(map(int, input().split()))
    max_sum = 0
    min_sum = 1000000
    for i in range(N-M+1):
        sum_V = 0
        for j in range(i, i+M):
            sum_V += V[j]
        if sum_V > max_sum:
            max_sum = sum_V
        if sum_V < min_sum:
            min_sum = sum_V
    cal_V = max_sum - min_sum
    print(f'#{tc+1} {cal_V}')