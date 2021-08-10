T = int(input())
for tc in range(T):
    N = int(input())
    Carrots = list(map(int, input().split()))
    worker1 = 0
    worker2 = 0
    count_worker1 = 0
    for i in range(0, N):
        if worker1 < worker2:
            worker1 += Carrots[0]
            Carrots.pop(0)
            count_worker1 += 1
        else:
            worker2 += Carrots[-1]
            Carrots.pop(-1)
    print(f'#{tc+1} {count_worker1} {abs(worker1 - worker2)}')