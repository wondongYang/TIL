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

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    nod_list = [input().split() for _ in range(E)]
    S, G = input().split()
    ans = nod(nod_list, S, G)
    print(f'#{tc+1} {ans}')
