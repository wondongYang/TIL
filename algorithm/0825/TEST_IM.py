T = int(input())
for tc in range(T):
    X, Y = map(int, input().split())

    m = min(X, Y)                   # x,y 중 최소값
    m_10 = (m * 10**4)//2           # 2h = m이 되는 때까지
    max_V = 0
    for i in range(0, m_10):
        h = i / 10**4               # step을 1/10**4로
        a = X-2*h
        b = Y-2*h
        v = h * a * b
        if v > max_V:
            max_V = v

    print(f'#{tc+1} {max_V:.6f}')


# 시간초과