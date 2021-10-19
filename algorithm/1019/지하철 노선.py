T = int(input())
for tc in range(T):
    N = int(input())
    passage = list(map(int, input().split()))
    possible_list = []

    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                for t in range(1, N+1):
                    V = 0
                    if abs(i-j) > 1 and abs(i-k) > 1 and abs(i-t) > 1 and abs(j-k) > 1 and abs(j-t) > 1 and abs(k-t) > 1 and i < k < j and i < t < j and k < t:
                        possible_list.append([i, j, k, t])
    check = possible_list[:]
    c = 0
    for i in range(len(check)):
        if check[i][0] == 1 and check[i][1] == N:
            i = i - c
            possible_list.pop(i)
            c += 1
    maxV = 0
    for i in range(len(possible_list)):
        V = (passage[possible_list[i][0]-1] + passage[possible_list[i][1]-1])**2 + (passage[possible_list[i][2]-1] + passage[possible_list[i][3]-1])**2
        if maxV < V:
            maxV = V
    for i in range(len(possible_list)):
        V = (passage[possible_list[i][0]-1] + passage[possible_list[i][2]-1])**2 + (passage[possible_list[i][1]-1] + passage[possible_list[i][3]-1])**2
        if maxV < V:
            maxV = V

    print(f'#{tc+1} {maxV}')





'''
5
10
80 90 65 55 90 60 40 35 30 25
8
30 25 70 55 95 75 90 20
10
60 85 45 25 15 70 55 70 85 35
15
80 30 35 95 45 85 30 25 100 85 10 60 80 30 5
20
45 30 5 85 55 85 10 5 75 60 15 65 45 50 75 80 15 10 50 90

#1 38425
#2 44225
#3 37925
#4 64850
#5 57850
'''

