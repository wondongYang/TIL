T = int(input())
for tc in range(T):
    N = int(input())
    Numbers = [list(map(int, input().split())) for _ in range(N)]
    ans = 0 # 모든 원소에 대해, 주변 원소와의 차이의 절대값의 합
    for i in range(N):
        for j in range(N):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj # i, j의 주변 ni, nj
                if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않으면
                    ans += abs(Numbers[i][j] - Numbers[ni][nj])
    print(f'# {tc+1} {ans}')