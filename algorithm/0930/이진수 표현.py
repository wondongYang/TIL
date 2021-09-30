T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    K = bin(M)
    ans = 'OFF'
    if len(K) >= N: 
        check = 0
        for i in range(N):
            if K[-1-i] == '1':
                check += 1
        if check == N:
            ans = 'ON'
    print(f'#{tc+1} {ans}')

'''
5
4 0
4 30
4 47
5 31
5 62
'''