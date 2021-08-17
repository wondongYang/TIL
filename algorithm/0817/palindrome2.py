for tc in range(10):
    T = int(input())
    N = 100
    Char = [input() for _ in range(N)]
    for M in range(100, 0, -1):
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
        print(final_ans)
        if final_ans != 0:
            break
    print(f'#{T} {len(final_ans)}')