def dfs(s, g, V):
    stack = []
    visited = [0] * (V+1)
    # 시작점
    n = s  # 현재 방문한 정점
    visited[n] = 1
    while n > 0: # 방문한 정점이 있으면
        # 현재 정점에 인접하고 방문하지 않은 정점 찾기
        for w in range(1, V+1):
            if adj[n][w] == 1 and visited[w] == 0: # w가 n에 인접하고 미방문이면
                stack.append(n)                    # 현재 위치를 경로로 저장
                n = w                              # w를 현재 위치로
                visited[n] = 1
                if n == g:                         # 방문한 정점에서 할 일 - 목적지 확인
                    return 1
                break                              # 현재 n을 기준으로 다시 w찾기
        else:                                      # w를 못찾은 경우. 지나온 정점을 꺼내 다른 w검색
            if stack:
                n = stack.pop()
            else:
                n = 0
    return 0


T = int(input())
for tc in range(T):
    V, E = map(int, input().split()) # 마지막 정점(정점개수), 간선 개수
    adj = [[0]*(V+1) for _ in range(V+1)] # 인접 행렬
    for _ in range(E): # 간선의 수 만큼 반복
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        # adj[n2][n1] = 1   # 간선에 방향이 없는 경우
    S, G = map(int, input().split())
    ans = dfs(S, G, V)
    print(f'#{tc+1} {ans}')