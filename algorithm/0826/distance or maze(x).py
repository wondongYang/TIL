def f(i, j, N):  # 출구를 찾으면 중단
    global count
    global mim_d
    if i == x2 and j == y2:   # 출구에 도착한 경우
        if min_d > len(count)-1:
            return len(count)-1
        else:
            return min_d
    else:
        count.append(0)
        m[i][j] = 9  # i, j 방문표시. (진입한 칸을 벽으로 변경)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and m[ni][nj] == 0:  # and visited[ni][nj]==0
                if f(ni, nj, N): # 출구를 찾고 리턴하면
                    return len(count)-1        # 입구까지 리턴(남겨둔 갈림길을 탐색하지 않음)
        for k in range(len(count)-1):
            count.pop()
        return 0

T = int(input())
for tc in range(T):
    N = int(input())
    m = [list(map(int, input())) for _ in range(N)]
    min_d = N * N
    count = []
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if m[i][j] == 2:
                x1 = i
                y1 = j
            elif m[i][j] == 3:
                x2 = i
                y2 = j
                m[i][j] = 0
    ans = f(x1, y1, N)
    print(f'#{tc+1} {ans}')