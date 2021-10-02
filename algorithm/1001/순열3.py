def f(N, R, i): # N개에서 R개를 고르는 순열, i 지금까지 고른 개수
    if i==R:
        print(p)
    else:
        for j in range(N):  # 사용하지 않은 숫자 찾기
            if u[j]==0:
                u[j] = 1    # 사용표시
                p[i] = a[j]
                f(N, R, i+1)
                u[j] = 0

N = 5
R = 3
a = [1,2,3,4,5]
u = [0]*N
p = [0]*R
f(N, R, 0)