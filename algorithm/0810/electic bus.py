T = int(input())
for tc in range(T):
    K_N_M = list(map(int, input().split()))
    K = K_N_M[0]
    N = K_N_M[1]
    M = K_N_M[2]
    Stop = list(map(int, input().split()))
    Stop.append(N)
    Stop.insert(0, 0)
    s_count = 0
    for i in range(1, N):
        K -= 1
        for j in range(len(Stop)-1):
            if Stop[j+1] - Stop[j] > K_N_M[0]:
                s_count = 0
                break
            elif K < Stop[j+1] - i and i == Stop[j]:
                s_count += 1
                K = K_N_M[0]
    print(f'#{tc+1} {s_count}')
