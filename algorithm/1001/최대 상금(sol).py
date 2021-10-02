def f(n, i, c):     # 배열의 길이, 교환 위치, 남은 교환횟수
    global maxV
    global maxC
    # 현재가 최대 상금인지 확인

    if i==n or c==0:    # 오른쪽에 교환할 원소가 없거나 남은 교환 횟수가 없으면
        s = 0
        for x in arr:
            s = s*10 + x
        if maxV<s:
            maxV = s
            maxC = c
        elif maxV == s and maxC>s:
            maxC = c
        return
    else:
        for j in range(n):
            if i!=j:
                arr[i], arr[j] = arr[j], arr[i]
                f(n, i+1, c-1)
                arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for tc in range(1, T+1):
    num, N = input().split()
    arr = list(map(int, num))
    maxV = 0
    maxC = 0
    f(len(arr), 0, int(N))
    print(f'#{maxV} {maxC}')