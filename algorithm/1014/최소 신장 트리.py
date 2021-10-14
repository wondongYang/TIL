def prim(start, V): # MST 가중치의 합을 리턴하는 함수, 1~V번 노드인 경우
    key = [INF] * (V + 1)   # key[i] i가 MST에 연결되는 비용
    key[start] = 0
    MST = [0] * (V + 1)
    pi = [0] * (V + 1)
    for _ in range(V):  # 모든 정점 MST에 포함될 때 까지
        # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
        u = 0
        minV = INF
        for i in range(1, V + 1):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1  # key[u]가 최소인 u를 MST에 추가
        for v in range(V + 1):  # u에 인접인 v에 대해
            if MST[v] == 0 and adjM[u][v] != 0:
                if key[v] > adjM[u][v]:  # u를 이용해 기존보다 더 작은 비용으로 갱신
                    key[v] = adjM[u][v]
                    pi[v] = u   # v는 u와 연결해서 MST에 포함될 예정
    return sum(key)

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    INF = 10000
    # 인접행렬
    adjM = [[0] * (V+1) for _ in range(V+1)]
    adjL = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w
        adjM[v][u] = w  # 가중치가 있는 무방향 그래프
        adjL[u].append((v, w))
        adjL[v].append((u, w))
    print(f'#{tc+1} {prim(0, V)}')