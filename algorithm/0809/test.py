T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    print(f'#{tc}', end=' ')
    for x in A:
        print(x, end= ' ')
    print()
