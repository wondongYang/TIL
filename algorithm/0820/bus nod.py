T = int(input())
for tc in range(T):
    N = int(input())
    nod_list = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop_list = []
    for i in range(P):
        stop_list.append([int(input()), 0])
    for i in range(N):
        for j in range(nod_list[i][0], nod_list[i][1]+1):
            for k in range(P):
                if j == stop_list[k][0]:
                    stop_list[k][1] += 1
    print(f'#{tc+1}', end=' ')
    for i in range(P):
        print(f'{stop_list[i][1]}', end=' ')
    print()
