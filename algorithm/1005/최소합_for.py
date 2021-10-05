# 시간초과 주의

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = [0] * 2 * (N-1)
    arr3 = []

    # 오른쪽으로 이동은 0, 아래로 이동은 1인 모든 이동 경우의 수 탐색
    for i in range(2**len(arr2)):
        arr2 = [0] * 2 * (N-1)
        k = i
        for j in range(len(arr2)):
            if k >= 2**(len(arr2)-1-j):
                arr2[j] = 1
                k -= 2**(len(arr2)-1-j)
        if arr2.count(0) == arr2.count(1):
            arr3.append(arr2)

    # 이동의 최소값 구하기        
    minV = 2 * 10 * N - 10
    for i in range(len(arr3)):
        p, t = 0, 0 # arr의 현재 위치
        sumV = arr[p][t]
        for j in range(len(arr3[i])):
            if arr3[i][j] == 0:
                t += 1
            else:
                p += 1
            sumV += arr[p][t]
        if minV >= sumV:
            minV = sumV
    print(f'#{tc+1} {minV}')


    
