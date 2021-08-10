T = int(input())
for tc in range(T):
    N = int(input())
    Carrots = list(map(int, input().split()))
    order_Carrot = 0
    max_Carrot = 0
    for i in range(N):
        if Carrots[i] > max_Carrot:
            order_Carrot = i+1
            max_Carrot = Carrots[i]
    print(f'#{tc+1} {order_Carrot} {max_Carrot}')