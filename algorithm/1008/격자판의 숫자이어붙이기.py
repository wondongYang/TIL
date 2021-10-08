di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def moving(i, j, num):
    if len(num) == 7:
        if num not in ans_list:
            ans_list.append(num)
        return
    else:
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < 4 and 0 <= nj < 4:
                moving(ni, nj, num + table[ni][nj])

T = int(input())
for tc in range(T):
    table = [list(input().split()) for _ in range(4)]
    ans_list = []
    for i in range(4):
        for j in range(4):
            moving(i, j, table[i][j])
    print(f'#{tc+1} {len(ans_list)}')
            