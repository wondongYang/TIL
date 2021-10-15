di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
o = [0, 2, 1, 4, 3] # 1, 2, 3, 4의 반대방향

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split()) # 셀의 크기, 격리 시간, 미생물 군집의 개수
    arr = [list(map(int, input().split())) for _ in range(K)]

    for t in range(M):  # 이동 시간
        moved = [[-1] * N for _ in range(N)]    # 이동 후 미생물 정보
        size = [[0] * N for _ in range(N)]
        for i in range(K):
            if arr[i][3] != 0:  # 아직 이동한느 군집이면
                arr[i][0] += di[arr[i][3]]   # 이동 후 세로
                arr[i][1] += dj[arr[i][3]]   # 이동 후 가로
                r, c = arr[i][0], arr[i][1]
                if r == 0 or r == N-1 or c == 0 or c == N-1:    # 가장자리
                    arr[i][2] //= 2 # 감소
                    if arr[i][2] > 0: # 미생물이 남으면
                        arr[i][3] = o[arr[i][3]]    # 반대방향으로
                    else:
                        arr[i][3] = 0   # 이동 제거
                else:   # 가장자리가 아니면
                    if moved[r][c] == -1:   # 다른 군집이 없으면
                        moved[r][c] = i # 군집번호 표시
                        size[r][c] = arr[i][2]  # 자리를 차지한 군집의 원래 미생물 수
                    else:   # 두 군집이 만나면
                        if arr[i][2] > size[r][c]:  # 새 군집이 비교대상 중 가장 크면
                            size[r][c] = arr[i][2]
                            arr[moved[r][c]][3] = arr[i][3] # 가장 큰 군집 방향 선택
                        arr[moved[r][c]][2] += arr[i][2]    #먼저 차지한 군집에 합침
                        arr[i][2] = 0   # 합쳐진 군집 소멸
                        arr[i][3] = 0   # 합쳐진 군집 이동 중지

    ans = 0
    for i in range(K):
        ans += arr[i][2]
    print(f'#{tc+1} {ans}')
