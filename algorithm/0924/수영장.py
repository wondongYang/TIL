def f(n, s):            # n월, s 이전까지의 비용
    global minV
    if n > 12:          # 모든날에 대한 고려가 끝났으면
        if minV > s:
            minV = s
    else:
        # 1개월치만 결제
        f(n+1, s + min(swim[n]*price[0], price[1]))  # n월에 1개월치만 결제하는 경우
        f(n+3, s + price[2])                         # n월에 3개월 이용권을 결제하는 경우

T = int(input())
for tc in range(T):
    price = list(map(int, input().split()))
    swim = [0] + list(map(int, input().split()))    # 1~12월을 인덱스로 사용
    minV = price[3]         # 1년 이용권을 초기값으로 
    f(1, 0)
    print(f'#{tc+1} {minV}')
    

'''
1개월부터 >> 가면서 계산
그달 계산하면서 앞의 2달치와 비교 계산(3개월권)
마지막에 1년치와 비교
'''
    