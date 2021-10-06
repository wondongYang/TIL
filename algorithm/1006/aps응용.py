def partition(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def quick_sort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quick_sort(A, l, s-1)
        quick_sort(A, s+1, r)

T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(f'#{tc+1}', end = ' ')
    for i in range(len(arr)):
        print(arr[i], end = ' ')
    print()

'''
3
11 45 23 81 28 34
11 45 22 81 23 34 99 22 17 8
1 1 1 1 1 0 0 0 0 0
'''