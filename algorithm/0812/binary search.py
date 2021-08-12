def binary_search(X, L, P):
    count = 0
    while True:
        if abs(L - X) == abs(P - X):
            count += 1
            break
        elif abs(L - X) > abs(P - X):
            L = int((L + P)/2)
            count += 1
        else:
            P = int((L + P)/2)
            count += 1
    return count

T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split())
    count_A = binary_search(A, 1, P)
    count_B = binary_search(B, 1, P)

    if count_A < count_B:
        winner = 'A'
    elif count_A > count_B:
        winner = 'B'
    else:
        winner = '0'
    print(f'#{tc+1} {winner}')
