def f(i, N): # P[i]의 값을 결정
    if i == N:
        print(P)
    else:
        for j in range(i, N): # P[i] <-> P[j] 자리교환
            P[i], P[j] = P[j], P[i]
            f(i + 1, N)
            P[i], P[j] = P[j], P[i]

P = [1, 2, 3]
f(0, 3)