def in_order(n):
    if n:
        in_order(left[n])
        print(node[n-1][1], end='')
        in_order(right[n])


for tc in range(10):
    N = int(input())
    node = [list(input().split()) for _ in range(N)]
    E = N - 1
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    path = []
    for i in range(N):
        for j in range(len(node[i])-2):
            path.append(int(node[i][0]))
            path.append(int(node[i][j+2]))

    for i in range(E):
        p, c = path[i * 2], path[i * 2 + 1]
        if left[p] == 0:  # p의 왼쪽 자식이 없으면
            left[p] = c
        else:  # 왼쪽 자식이 있으면 오른쪽자식으로 저장
            right[p] = c
    print(f'#{tc+1}', end=' ')
    in_order(1)
    print()