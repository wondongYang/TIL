T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    list_A = list(range(1, 13))
    list_sub = []
    ans = 0
    for i in range(1 << 12):
        list_subset = []
        for j in range(12):
            if i & (1 << j):
                list_subset.append(list_A[j])
        if len(list_subset) == N:
            list_sub.append(list_subset)
    for i in list_sub:
        if sum(i) == K:
            ans += 1
    print(f'#{tc+1} {ans}')
