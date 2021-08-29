def check(table):
    for i in range(9):
        check_row = sorted(table[i])
        check_table = check_row[:]
        for j in range(1, 10):
            if j == check_table[j-1]:
                check_row.pop(0)
        if len(check_row) > 0:
            return 0

    check_col = []
    for i in range(9):
        for j in range(9):
            check_col.append(table[j][i])
        check_col.sort()
        check_table = check_col[:]
        for j in range(1, 10):
            if j == check_table[j - 1]:
                check_col.pop(0)
        if len(check_col) > 0:
            return 0

    check_box = []
    check_i = 0
    check_j = 0
    for _ in range(9):
        for i in range(9):
            for j in range(9):
                if i // 3 == check_i and j // 3 == check_j:
                    check_box.append(table[i][j])
                if len(check_box) == 9:
                    check_box.sort()
                    check_table = check_box[:]
                    for k in range(1, 10):
                        if k == check_table[k - 1]:
                            check_box.pop(0)
                    if len(check_box) > 0:
                        return 0
        check_j += 1
        if check_j == 3:
            check_j = 0
            check_i += 1
    return 1

T = int(input())
for tc in range(T):
    table = [list(map(int, input().split())) for _ in range(9)]
    ans = check(table)
    print(f'#{tc+1} {ans}')