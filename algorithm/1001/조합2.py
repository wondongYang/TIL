# n개에서 r개를 고르는 조합, s 선택 구간의 시작, k 고른개수

def nCr(n, r, s, k):
    if k==r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1): # n-r+k 선택할 수 있는 구간의 끝
            comb[k] = i
            nCr(n, r, i+1, k+1)

N = 10
R = 3
comb = [0]*R
nCr(N, R, 0, 0)