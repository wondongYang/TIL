def f(u, N):
    visited[u] = 1
    r = 0
    for v in range(1, N+1):
        if adjM[u][v]==1 and visited[v]==0:
            r = max(r, f(v, N))
    visited[u] = 0
    return r + 1
 
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjM=[[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adjM[n1][n2] = 1
        adjM[n2][n1] = 1
    visited = [0]*(N+1)
    ans = 0
    for i in range(1, N+1):
        ans = max(ans, f(i, N))
    print(f'#{tc} {ans}')
