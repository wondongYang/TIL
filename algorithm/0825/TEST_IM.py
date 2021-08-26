T = int(input())
for tc in range(T):
    X, Y = map(int, input().split())
    h = min(X, Y) / 4
    d = h / 2
    ans = 0
    while True:
        h1 = h + d
        h2 = h - d
        V1 = (X - 2 * h1) * (Y - 2 * h1) * h1
        V2 = (X - 2 * h2) * (Y - 2 * h2) * h2
        if abs(V1 - V2) < 1e-7:
            ans = V1
            break
        else:
            if V1 > V2:
                h = h1
            else:
                h = h2
        d /= 2
    print(f'#{tc+1} {V1:.6f}')