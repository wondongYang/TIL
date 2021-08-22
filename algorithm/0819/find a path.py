def nod(nod_list, S, G):
    S_list = []
    F = 0
    for i in range(E):
        if nod_list[i][1] == G:
            S_list.append(nod_list[i][0])
    if S_list:
        for i in S_list:
            if i == S:
                return 1
            else:
                F += nod(nod_list, S, i)
        return F
    else:
        return 0

for tc in range(10):
    T, E = map(int, input().split())
    nod_list1 = list(map(int, input().split()))
    nod_list2 = [[0, 0] for _ in range(E)]
    for i in range(0, E):
        nod_list2[i][0] = nod_list1[2*i]
        nod_list2[i][1] = nod_list1[(2*i)+1]
    print(nod_list2)
    S, G = 0, 99
    ans = nod(nod_list2, S, G)
    if ans > 0:
        final_ans = 1
    else:
        final_ans = 0
    print(f'#{T} {final_ans}')