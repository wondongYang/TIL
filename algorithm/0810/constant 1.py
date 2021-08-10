T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, str(input())))
    numbers.append(0)
    count_1 = 0
    list_count = [0]
    max_count = 0
    for i in range(N+1):
        if numbers[i] == 1:
            count_1 += 1
        else:
            list_count.append(count_1)
            count_1 = 0
        for j in list_count:
            if j > max_count:
                max_count = j
    print(f'#{tc+1} {max_count}')