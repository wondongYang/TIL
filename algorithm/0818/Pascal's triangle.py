T = int(input())
for tc in range(T):
    N = int(input())
    tri = [[0] * N for _ in range(N)]
    for i in range(N):
        tri[i][0] = 1
        for j in range(1, i+1):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
    for i in range(N):
        for j in range(N-i-1):
            tri[i].pop()
    print(f'#{tc+1}')
    for i in range(N):
        for j in range(i+1):
            print(tri[i][j], end=' ')
        print('')

