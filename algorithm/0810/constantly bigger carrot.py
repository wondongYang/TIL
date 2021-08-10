T = int(input())
for tc in range(T):
    N = int(input())
    Carrots = list(map(int, input().split()))
    Carrots.append(0)
    list_count = []
    count_constant = 1
    max_count = 0
    for i in range(N):
        if Carrots[i+1] > Carrots[i]:
            count_constant += 1
        else:
            list_count.append(count_constant)
            count_constant = 1
        for j in list_count:
            if j > max_count:
                max_count = j
    print(f'#{tc+1} {max_count}')

