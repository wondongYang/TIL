def paper(N):
    count = 0
    if N == 10:
        count += 1
        return count
    elif N == 20:
        count += 3
        return count
    else:
        return paper(N-10) + 2 * paper(N-20)

T = int(input())
for tc in range(T):
    N = int(input())
    K = paper(N)
    print(f'#{tc+1} {K}')