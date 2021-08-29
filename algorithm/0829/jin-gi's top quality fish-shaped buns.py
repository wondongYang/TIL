T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    arriving_time = list(map(int, input().split()))
    arriving_time.sort()
    time = []
    bread = 0
    i = 0
    while bread < N:
        i += 1
        if i % M == 0:
            bread += K
            time.append(i)
    check = len(arriving_time)
    for j in range(len(arriving_time)):
        if time[j // K] <= arriving_time[j]:
            check -= 1
    if check == 0:
        print(f'#{tc+1} Possible')
    else:
        print(f'#{tc+1} Impossible')



