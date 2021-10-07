def hoare(A, l, r):
    i, j = l, r
    x = A[l]
    while i <= j:
        while i <= j and A[i] <= x:
            i += 1
        while i <= j and A[j] >= x:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def qsort(A, l, r):
    if l < r:
        p = hoare(A, l, r)
        qsort(A, l, p-1)
        qsort(A, p+1, r)


T = int(input())
for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    qsort(A, 0, N-1)
    print(f'#{tc+1} {A[N//2]}')