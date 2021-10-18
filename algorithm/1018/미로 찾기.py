di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def f(i, j, k, t):    # 출발좌표, 도착좌표, 이동거리
    global ans
    arr[i][j] = 1   # 방문했으면 벽으로 변경
    if i == k and j == t:  # 도착지에 도달하면 
        ans = 1
        return
    else:
        for p in range(4):  # 4방향 탐색
            ni, nj = i + di[p], j + dj[p]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and arr[ni][nj] != 4:
                f(ni, nj, k, t)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 2와 3의 좌표 찾기
    a, b, c, d = 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                a, b = i, j
            if arr[i][j] == 3:
                c, d = i, j
    f(a, b, c, d)
    print(f'#{tc+1} {ans}')