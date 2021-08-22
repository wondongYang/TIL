T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    m = list(map(int, input().split()))
    max_profit = 0  # 최대이익 이익들의 합
    best = m[-1]  # 마지막 날 값을 최대라고 가정

    for i in range(n - 1, -1, -1):  # 뒤에서부터 비교
        if m[i] > best:  # 마지막날보다 값이 크면
            best = m[i]  # 최대가격 변경
        else:
            max_profit += best - m[i]  # 아니면 최대에서 가격 빼서 이익 추가

    print(f'#{tc} {max_profit}')