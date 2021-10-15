dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS():
    Q = [0] * 100000
    front = rear = -1

    rear += 1
    Q[rear] = (0, 0)    # 행과 열의 좌표를 넣는다.
    dist[0][0] = 0

    while front != rear:
        front += 1
        r, c = Q[front]

        # 4방향 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                power = arr[nr][nc] - arr[r][c] if arr[nr][nc] > arr[r][c] else 0
                if dist[nr][nc] > dist[r][c] + power + 1:
                    rear += 1
                    Q[rear] = (nr, nc)
                    dist[nr][nc] = dist[r][c] + power + 1


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]

    BFS()

    print(f'#{tc+1} {dist[N-1][N-1]}')