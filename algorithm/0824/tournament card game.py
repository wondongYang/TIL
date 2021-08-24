def f(P):
    g1 = []
    g2 = []
    if len(P) == 1:
        return [P[0]]
    elif len(P) == 2:
        if P[0][1] == P[1][1] or P[0][1] - P[1][1] == 1 or P[0][1] - P[1][1] == -2:
            return [P[0]]
        else:
            return [P[1]]
    else:
        for i in range(len(P)):
            if i <= (len(P)+1)//2 - 1:
                g1.append(P[i])
            else:
                g2.append(P[i])
        return f(f(g1) + f(g2))

T = int(input())
for tc in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    for i in range(N):
        P[i] = [i+1, P[i]]
    ans = f(P)
    print(f'#{tc+1} {ans[0][0]}')