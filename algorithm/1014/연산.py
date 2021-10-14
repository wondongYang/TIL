def bfs(N, M):
    global ans
    q = [N]
    while q:
        N = q.pop(0)
        if N == M:
            ans = visited[N]
            return
        for c in [N+1, N-1, N*2, N-10]:
            if 1 <= c <= 1000000 and visited[c] == 0:
                q.append(c)
                visited[c] = visited[N] + 1

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    ans = 0
    visited = [0] * 1000001
    bfs(N, M)
    print(f'#{tc+1} {ans}')
