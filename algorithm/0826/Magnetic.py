for tc in range(10):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    check = [0, 0]
    count = 0

    for i in range(N):
        check = [0, 0]
        for j in range(N):
            if table[j][i] == 1:
                check[0] = 1
            elif table[j][i] == 2 and check[0] == 1:
                check[1] = 2
            if check == [1, 2]:
                count += 1
                check = [0, 0]
    print(f'#{tc+1} {count}')