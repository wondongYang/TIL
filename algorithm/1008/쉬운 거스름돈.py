T = int(input())
for tc in range(T):
    M = int(input())
    S = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = []
    for i in range(len(S)):
        ans.append(M//S[i])
        M -= (M//S[i]) * S[i]
    print(f'#{tc+1}')
    for i in range(len(ans)):
        print(ans[i], end = ' ')
    print()