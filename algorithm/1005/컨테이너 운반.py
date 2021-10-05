T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    cont = list(map(int, input().split()))  # 화물 리스트
    truck = list(map(int, input().split())) # 트럭 리스트
    sumV = 0    # 옮긴 화물 무게의 합
    while len(truck) > 0 and len(cont) > 0: # 화물과 트럭이 모두 남아 있다면
        maxT = 0    # 적재용량이 가장 큰 트럭 탐색
        for i in range(len(truck)):
            if maxT < truck[i]:
                maxT = truck[i]
        maxC = 0    # 가장 무거운 화물 탐색
        for i in range(len(cont)):
            if maxC < cont[i]:
                maxC = cont[i]
        if maxT >= maxC:    # 적재용량이 화물보다 크다면 운송
            truck.remove(maxT)
            cont.remove(maxC)
            sumV += maxC
        else:   # 적재용량이 화물보다 작으면 화물을 제거
            cont.remove(maxC)
    print(f'#{tc+1} {sumV}')
    
        

