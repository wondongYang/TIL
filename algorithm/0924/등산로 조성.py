def f(i, j, N, K, c, s):    # i, j 칸이 등산로에 포함, 깍는 횟수 c, 이전까지의 길이 s
    global maxV         # 최대 등산로 길이
    if maxV < s+1:     
        maxV = s+1      # 최대 등산로 길이 갱신
    v[i][j] = 1         # 현재 등산로에 포함된 칸
    # 주변 칸 탐색
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
            if mount[i][j] > mount[ni][nj]: # 더 낮은 경우
                f(ni, nj, N, K, c, s+1)
            elif c == 1 and mount[i][j] > mount[ni][nj] - K:    # 깍고 이동할 수 있는 경우
                tmp = mount[ni][nj] # 원래 높이 저장
                mount[ni][nj] = mount[i][j] - 1
                f(ni, nj, N, K, c-1, s+1)
                mount[ni][nj] = tmp
    v[i][j] = 0     # i, j 칸을 이전의 다른 경로에서 사용할 수 있도록
 
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    mount = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]   # 현재 등산로에 포함된 칸 표시
    # 최대 높이 찾기
    h = 0 # 최대 높이
    for i in range(N):
        for j in range(N):
            if h < mount[i][j]:
                h = mount[i][j]
    # 최대 높이인 곳에서 등산로 만들어보기
    maxV = 0    # 최대 등산로 길이
    for i in range(N):
        for j in range(N):
            if mount[i][j] == h:
                f(i, j, N, K, 1, 0) # i, j 에서부터 등산로 만들어 보기, 깍을 수 있는 횟수, 지금까지의 등산로 길이
    
    print(f'#{tc+1} {maxV}')
