T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(input().split())
    deck_1 = []
    deck_2 = []
    if N % 2 == 0:
        for i in range(N):
            if i < N/2:
                deck_1.append(cards[i])
            else:
                deck_2.append(cards[i])
        print(f'#{tc+1}', end=' ')
        for i in range(int(N/2)):
            print(deck_1[i], end=' ')
            print(deck_2[i], end=' ')
    else:
        for i in range(N):
            if i < N/2:
                deck_1.append(cards[i])
            else:
                deck_2.append(cards[i])
        print(f'#{tc+1}', end=' ')
        for i in range(N//2):
            print(deck_1[i], end=' ')
            print(deck_2[i], end=' ')
        print(deck_1[-1], end=' ')
    print()



