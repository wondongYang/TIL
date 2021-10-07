def binary_search(l, r, num, direction):
    global c
    if l > r:
        return
    m = (l+r)//2
    if A[m] == num:     # 같으면
        c += 1
        return 
    elif A[m] < num:    # 오른쪽 구간 선택
        if direction == 1:
            return
        return binary_search(m+1, r, num, 1)
    else:               # 왼쪽 구간 선택
        if direction == 2:
            return
        return binary_search(l, m-1, num, 2)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    c = 0
    for i in B:
        binary_search(0, N-1, i, 0)
    print(f'#{tc+1} {c}')
