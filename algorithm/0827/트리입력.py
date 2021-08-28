'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
6
1 2 1 3 2 4 3 5 3 6
'''

def pre_order(n):
    if n:           # 유효한 정점이면
        print(n, end = ' ')
        pre_order(left[n])          # n의 왼쪽자식으로 이동
        pre_order(right[n])

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
par = [0]*(V+1)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:    # p의 왼쪽 자식이 없으면
        left[p] = c
    else:               # 왼쪽 자식이 있으면 오른쪽자식으로 저장
        right[p] = c
    par[c] = p   # (1) 조상을 찾는데 사용
                 # (2) root 찾기

c = 6
while par[c]:
    print(par[c])
    c = par[c]

# 부모가 없으면 root
root = 1
while par[root]: # root로 추정한 정점이 부모가 있으면
    root += 1
print(root)

pre_order(1)
print()
in_order(1)
print()
post_order(1)