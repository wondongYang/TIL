def f(i, k):
    global minS
    if i == k:    # 경로 한개 완성
        s = bat[0][A[0]]    # 사무실 -> 첫 경유지
        for j in range(k-1):    # 경유지의 출발지 인덱스
            s += bat[A[j]][A[j+1]]
        s += bat[A[k-1]][0]     # 마지막 경유지 -> 사무실
        if minS >= s:
            minS = s   
    else:
        for j in range(i, k):
            A[i], A[j] = A[j], A[i]
            f(i + 1, k)
            A[i], A[j] = A[j], A[i]

T = int(input())
for tc in range(T):
    N = int(input())
    bat = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(1, N)]
    minS = 100 * N
    f(0, N-1)
    print(f'#{tc+1} {minS}')
