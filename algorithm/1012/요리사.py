def f(food1):
    global min_s

    # 음식1의 시너지 합
    s1 = 0
    for i in food1:
        for j in range(N):
            if j in food1:
                s1 += food[i][j]

    # 음식2의 구성
    food2 = total[:]
    for i in range(N-1, -1, -1):
        for j in range(R-1, -1, -1):
            if total[i] == food1[j]:
                food2.pop(i)

    # 음식2의 시너지 합
    s2 = 0
    for i in food2:
        for j in range(N):
            if j in food2:
                s2 += food[i][j]

    # 음식1과 음식2의 최소 차이
    ans = abs(s1-s2) 
    if min_s > ans:
        min_s = ans 

# 음식1의 구성
def nCr(n, r, s, k):
    if k==r:
        return f(comb)
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            nCr(n, r, i+1, k+1)

T = int(input())
for tc in range(T):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    R = int(N / 2)
    total = [i for i in range(N)]
    comb = [0]*R
    min_s = 20000 * (N/2-1) ** 2
    nCr(N, R, 0, 0)
    print(f'#{tc+1} {min_s}')

