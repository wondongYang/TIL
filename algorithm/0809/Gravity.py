T = int(input())
for k in range(T):
    N = int(input())
    B = list(map(int, input().split()))
    max_box = 0
    for i in range(0, N):
        count_i = 0
        for j in range(i+1, N):
            if B[i] > B[j]:
                count_i += 1
        if max_box < count_i:
            max_box = count_i
    c = k+1
    print(f'#{c} {max_box}')
