T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = []
    for i in range(len(pizza)):
        pizza[i] = [i+1, pizza[i]]
    for i in range(N):
        oven.append(pizza.pop(0))
    while len(oven) > 1:
        oven[0][1] //= 2
        check = oven.pop(0)
        if check[1] == 0:
            if len(pizza) != 0:
                oven.append(pizza.pop(0))
        else:
            oven.append(check)
    print(f'#{tc+1} {oven[0][0]}')