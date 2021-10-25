def perm(n, k): # 순열 만들기
    if k==n:
        a = p[:]
        P_list.append(a)
        return
    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(n, k+1)
            p[k], p[i] = p[i], p[k]

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minS = 99*N     # 최소값 설정 = 99이하의 정수 x N개
    p = [i for i in range(N)]
    P_list = []
    perm(N, 0)
    for i in range(len(P_list)):
        s = 0
        for j in range(N):
            s += arr[j][P_list[i][j]]   # 순열에 따른 합구하기
        if minS > s:
            minS = s
    print(f'#{tc+1} {minS}')


# 순열을 짜서 숫자를 뽑아내기...
# 123 132 213 231 312 321

'''
1
3
96 78 61
78 64 67
29 40 59

#1 154
'''