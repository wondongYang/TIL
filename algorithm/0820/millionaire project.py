T = int(input())
for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    profit = 0
    max_price = price[-1]
    for i in range(N-2, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            profit += max_price - price[i]

    print(f'#{tc+1} {profit}')
