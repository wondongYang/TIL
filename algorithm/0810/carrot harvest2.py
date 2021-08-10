T = int(input())
for tc in range(T):
    N_M = list(map(int, input().split()))
    N = N_M[0]
    M = N_M[1]
    Carrots = list(map(int, input().split()))
    Cart = 0
    distance = 0
    for i in range(N):
        for j in range(Carrots[i]):
            Cart += 1
            if Cart == M:
                distance += 2 * (i+1)
                Cart = 0
    print(f'#{tc+1} {distance + (2*N)}')
