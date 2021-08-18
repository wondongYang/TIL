



T = int(input())
for tc in range(T):
    N = int(input())
    print(f'#{tc+1}')
    for i in range(1, N+1):
        print(*[i] * i)

