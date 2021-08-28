def pre_order(n):
    global cnt
    if n:           # 유효한 정점이면
        cnt += 1
        pre_order(left[n])          # n의 왼쪽자식으로 이동
        pre_order(right[n])

def node(n):
    if n:
        r1 = node(left[n])
        r2 = node(right[n])
        return r1 + r2 + 1
    else:
        return 0

def in_order(n):
    if n:
        in_order(left[n])
        print(n, end = ' ')
        in_order(right[n])

def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n, end = ' ')

V = int(input())
edge = list(map(int, input().split()))
E = V -1    # V개의 정점이 있는 트리의 간선 수
left = [0]*(V+1)    # 부모를 인덱스로 자식번호 저장
right = [0]*(V+1)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:    # p의 왼쪽 자식이 없으면
        left[p] = c
    else:               # 왼쪽 자식이 있으면 오른쪽자식으로 저장
        right[p] = c

cnt = 0
pre_order(1)        # 1의 자손 수 찾기... 서브트리의 루트 제외
print(cnt - 1)