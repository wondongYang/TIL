T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    Numbers = list(map(int, input().split()))
    while M > 0:
        Numbers.append(Numbers.pop(0))
        M -= 1
    print(f'#{tc+1} {Numbers[0]}')
