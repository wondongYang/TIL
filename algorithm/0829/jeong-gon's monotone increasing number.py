def mono_incre(num):
    num_list = []
    while num > 0:
        num_list.append(num % 10)
        num //= 10
    for i in range(1, len(num_list)):
        if num_list[i] <= num_list[i - 1]:
            continue
        else:
            return 0
    return 1

T = int(input())
for tc in range(T):
    N = int(input())
    Num = list(map(int, input().split()))
    max_cross = -1
    for i in range(N-1):
        for j in range(i+1, N):
            if mono_incre(Num[i] * Num[j]) == 1:
                if max_cross < Num[i] * Num[j]:
                    max_cross = Num[i] * Num[j]
    print(f'#{tc+1} {max_cross}')

