def f(n): # 순회하는 함수
    global cnt
    if n:
        cnt += 1
        f(ch1[n])
        f(ch2[n])

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    V = E + 1 # 1번부터 V번까지 정점번호
    ch1 = [0] * (V+1) # 자식1 혹은 왼쪽자식, 부모를 인덱스로 자식번호 저장
    ch2 = [0] * (V+1) # 자식2 혹은 오른쪽자식
    arr = list(map(int, input().split()))
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1] # 부모 n1, 자식 n2
        if ch1[n1] == 0: # 자식1이 아직 없으면
            ch1[n1] = n2
        else:
            ch2[n1] = n2
    cnt = 0     # 방문한 정점 수
    f(N)        # N부터 순회...
    print(f'#{tc+1} {cnt}')
