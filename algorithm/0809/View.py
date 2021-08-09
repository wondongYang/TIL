for t in range(1, 11):
    N = int(input())
    B = list(map(int, input().split()))
    sum_V = 0
    for i in range(2, N-2):
        V = 0
        if B[i] > B[i+1] and B[i] > B[i+2] and B[i] > B[i-1] and B[i] > B[i-2]:
            if B[i+1] >= B[i+2] and B[i+1] >= B[i-1] and B[i+1] >= B[i-2]:
                V = B[i] - B[i+1]
            elif B[i+2] >= B[i-1] and B[i+2] >= B[i-2] and B[i+2] >= B[i+1]:
                V = B[i] - B[i+2]
            elif B[i-1] >= B[i+2] and B[i-1] >= B[i+1] and B[i-1] >= B[i-2]:
                V = B[i] - B[i-1]
            else:
                V = B[i] - B[i-2]
        sum_V += V
    print(f'#{t} {sum_V}')
