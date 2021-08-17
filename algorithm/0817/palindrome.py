T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    Char = [input() for _ in range(N)]
    final_ans = 0
    for i in range(N):
        for j in range(N-M+1):
            ans = ''
            for k in range(M):
                ans += Char[k+j][i]
            if ans == ans[::-1]:
                final_ans = ans
    for i in range(N):
        for j in range(N-M+1):
            ans = Char[i][j:j+M]
            if ans == ans[::-1]:
                final_ans = ans[:]
    print(f'#{tc+1} {final_ans}')





