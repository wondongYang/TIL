def dfs1(i, j, N):
    global cnt
    visited[i][j] = 1
    cnt += 1
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
            dfs1(ni, nj, N)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

ans = 0
visited = [[0] * N for _ in range(N)]
block = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            cnt = 0
            ans += 1
            dfs1(i, j, N)
            block.append(cnt)

print(ans)
block.sort()
for s in block:
    print(s)


'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''