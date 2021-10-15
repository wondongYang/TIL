def dijkstra(adj, D, X, N):
    # U = {X}
    U = [0] * (N+1)
    U[X] = 1
    # X에서 나머지 집으로 가는 비용 초기화
    for i in range(1, N+1):
        D[i] = adj[X][i]
    # N-1개 집의 최소 비용 결정
    for _ in range(N-1):
        # U[X] ==0, D[w]가 최소인 w찾기
        w = 0
        minV = INF
        for i in range(1, N+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        # w는 비용 결정
        U[w] = 1
        # w에 인접인 v에 대해 D[v]. D[w] + adj[w][v] 중 작은 값 선택
        for v in range(1, N+1):
            if 0 < adj[w][v] < INF:
                D[v] = min(D[v], D[w] + adj[w][v])


T = int(input())
for tc in range(T):
    N, M, X = map(int, input().split())     # 사람수, 간선수, 파티집
    INF = 987654321
    adjM = [[INF] * (N+1) for _ in range(N+1)]    # 인접행렬
    adjMR = [[INF] * (N+1) for _ in range(N+1)]     # 뒤집은행렬
    for i in range(1, N+1):
        adjM[i][i] = 0
        adjMR[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split()) # c 가중치
        adjM[x][y] = c
        adjMR[y][x] = c
    Din = [0] * (N+1)
    Dout = [0] * (N+1)
    dijkstra(adjMR, Din, X, N)
    dijkstra(adjM, Dout, X, N)

    # 최대 왕복시간
    maxV = 0
    for i in range(1, N+1):
        if maxV < Din[i] + Dout[i]:
            maxV = Din[i] + Dout[i]
    print(f'#{tc+1} {maxV}')


        