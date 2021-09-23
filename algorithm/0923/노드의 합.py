def f(n, V):
    if n > V:               # 없는 노드인 경우
        return 0
    else:
        if tree[n] > 0:     # 리프노드에 도착하면
            return tree[n]  # 이미 값이 있으므로 리턴
        else:
            r1 = f(2*n, V)
            r2 = f(2*n+1, V)
            tree[n] = r1 + r2
            return tree[n]

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split()) # N 마지막 정점, M 리프노트 수, L 출력할 정점
    tree = [0] * (N+1)                  # 비어있는 완전트리 생성
    for _ in range(M):                  # M개의 리프노드에 값 저장
        index, data = map(int, input().split())
        tree[index] = data
    f(1, N)                             # 순회하면서 힙을 저장
    print(f'#{tc+1} {tree[L]}')
  