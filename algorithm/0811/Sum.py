for tc in range(10):
    N = int(input())
    Numbers = [list(map(int, input().split())) for _ in range(100)]
    row_list = []
    col_list = Numbers[0][:]
    cross_list = []
    cross_sum = 0
    sum_cross = 0
    for i in range(100):
        row_list.append(sum(Numbers[i]))
        for j in range(1, 100):
            col_list[i] += Numbers[j][i]
        for k in range(100):
            if i == k:
                cross_sum += Numbers[i][k]
            if i + k == 99:
                sum_cross += Numbers[i][k]
    cross_list.append(cross_sum)
    cross_list.append(sum_cross)
    final_list = row_list + col_list + cross_list
    print(f'#{N} {max(final_list)}')





