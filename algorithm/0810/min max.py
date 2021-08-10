T = int(input())
for tc in range(T):
    N = int(input())
    a_i = list(map(int, input().split()))
    max_a = a_i[0]
    min_a = a_i[0]
    for i in range(len(a_i)):
        if a_i[i] > max_a:
            max_a = a_i[i]
        elif a_i[i] < min_a:
            min_a = a_i[i]
    a_dif = max_a - min_a
    print(f'#{tc+1} {a_dif}')