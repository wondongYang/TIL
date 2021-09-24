dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dist = [[987654321] * M for _ in range(N)] # 방문 체크 겸 거리 체크
    
    Q = [0] * (N * M)
    front = -1
    rear = -1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                rear += 1
                Q[rear] = (i, j)
                dist[i][j] = 0
    while front != rear:
        front += 1
        r, c = Q[front]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:
                dist[nr][nc] = dist[r][c] + 1
                rear += 1
                Q[rear] = (nr, nc)

    ans = 0

    for i in dist:
        for j in i:
            ans += j
    
    print(f'#{tc+1} {ans}')



