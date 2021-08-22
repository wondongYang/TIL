def sudoku(table):

    # 가로 체크
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
                if table[i][j] == table[i][k]:
                    return 0

    # 세로 체크
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9):
                if table[j][i] == table[k][i]:
                    return 0

    # 3 x 3 체크
    for k in range(3):
        for t in range(3):
            check_list = []
            for i in range(9):
                for j in range(9):
                    if i // 3 == k and j // 3 == t:
                        check_list.append(table[i][j])
                    if len(check_list) == 9:
                        break
            for i in range(9):
                for j in range(i+1, 9):
                    if check_list[i] == check_list[j]:
                        return 0

    return 1

T = int(input())
for tc in range(T):
    table = [list(map(int, input().split())) for _ in range(9)]
    ans = sudoku(table)
    print(f'#{tc+1} {ans}')
