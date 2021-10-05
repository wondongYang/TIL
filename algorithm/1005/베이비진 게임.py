T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    p1 = [] # player1의 카드
    p2 = [] # player2의 카드
    ans = 0 # 승리한 player

    # 카드배분
    for i in range(len(arr)):
        if i % 2 == 0:
            p1.append(arr[i])
        else:
            p2.append(arr[i])

        if len(p1) >= 3:    # 보유한 카드의 개수가 3개 이상일 때부터 판별
            p1.sort()       # 카드를 순서대로 정렬
            for j in range(len(p1)-2):
                if p1[j] == p1[j+1] == p1[j+2]: # triplet 판별
                    ans = 1
                    break
            p1_run = list(set(p1))  # 중복을 제거
            for j in range(len(p1_run)-2):
                if p1_run[j] + 2 == p1_run[j+1] + 1 == p1_run[j+2]: # run 판별
                    ans = 1
                    break
            if ans != 0:    # 승리자가 있다면 카드배분 중지
                break

        # player2도 동일한 판별 실시
        if len(p2) >= 3:    
            p2.sort()
            for j in range(len(p2)-2):
                if p2[j] == p2[j+1] == p2[j+2]:
                    ans = 2
                    break
            p2_run = list(set(p2))  
            for j in range(len(p2_run)-2):  
                if p2_run[j] + 2 == p2_run[j+1] + 1 == p2_run[j+2]:
                    ans = 2
                    break
            if ans != 0:
                break
    print(f'#{tc+1} {ans}')