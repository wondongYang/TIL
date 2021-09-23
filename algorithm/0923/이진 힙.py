def enq(data):
    global last
    last += 1       # 완전이진트리 유지(마지막 정점 추가)
    tree[last] = data
    c = last        # 새 정점을 자식으로
    p = c//2
    while p > 0 and tree[p] > tree[c]:      #부모가 존재하고, 최소힙 규칙에 어긋나면
        tree[p], tree[c] = tree[c], tree[p] # 교환
        c = p                               # 부모를 새로운 자식으로
        p = c//2
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0        # 힙의 마지막 정점
    for x in arr:
        enq(x)
    k = 0
    while N > 0:
        N //= 2
        k += tree[N]
    print(f'#{tc} {k}')