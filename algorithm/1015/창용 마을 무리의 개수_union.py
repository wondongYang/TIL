def find_set(x):
    if x == rep[x]:
        return x
    else:
        return find_set(rep[x])

def union(x, y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    edge = []
    for _ in range(M):
        u, v = map(int, input().split())
        edge.append([u, v])
    rep = [i for i in range(N+1)]       # 대표원소 배열
    for i in range(M):
        x, y = edge[i][0], edge[i][1]
        union(x, y)

    ans = set()
    for i in range(1, N+1):
        ans.add(find_set(i))
    print(f'#{tc+1} {len(ans)}')