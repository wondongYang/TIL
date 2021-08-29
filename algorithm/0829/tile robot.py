T = int(input())
for tc in range(T):
    N = int(input())
    robot = [list(map(int, input().split())) for _ in range(N)]
    tile = [[0] * 10 for _ in range(10)]
    for i in range(N):
        for j in range(robot[i][0], robot[i][2]+1):
            for k in range(robot[i][1], robot[i][3]+1):
                tile[j][k] = 1
    count = 0
    for i in range(10):
        for j in range(10):
            if tile[i][j] == 1:
                count += 1
    print(f'#{tc+1} {count}')