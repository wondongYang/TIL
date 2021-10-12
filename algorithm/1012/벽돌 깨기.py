def f(arr, N, W, H):   # N 남은 발사 횟수
    global minV
    if N == 0:  # 남은 발사 횟수가 없으면 남은 벽돌 세기
        c = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    c += 1
        if minV > c:
            minV = c
    else:       # 구슬을 발사할 수 있으면
        for k in range(W):      # k 구슬을 발사할 위치
            new_arr = [[0] * W for _ in range(H)]
            for i in range(H):  # 구슬을 발사할 복사본 만들기
                for j in range(W):
                    new_arr[i][j] = arr[i][j]
            # 발사...
            r = 0
            while r < H and new_arr[r][k] == 0:     # 구슬을 발사한 위치의 맨 윗 벽돌 찾기
                r += 1
            if r < H:
                boom = [(r, k, new_arr[r][k])]      # 깨지는 벽돌
                new_arr[r][k] = 0
                while boom:
                    i, j, t = boom.pop(0)
                    for p in range(1, t):
                        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                            ni, nj = i + di * p, j + dj * p
                            if 0 <= ni < H and 0 <= nj < W and new_arr[ni][nj] > 0:
                                boom.append((ni, nj, new_arr[ni][nj]))
                                new_arr[ni][nj] = 0
            # 벽돌 빈칸 채우기
            for j in range(W): 
                s = []
                for i in range(H-1, -1, -1):
                    if new_arr[i][j]:
                        s.append(new_arr[i][j])
                        new_arr[i][j] = 0
                for i in range(len(s)):
                    new_arr[H-1-i][j] = s[i]

            # N-1
            f(new_arr, N-1, W, H)


T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    minV = W*H      # 최소로 남은 별돌
    f(arr, N, W, H)            # 남은 발사 횟수
    print(f'#{tc+1} {minV}')
    