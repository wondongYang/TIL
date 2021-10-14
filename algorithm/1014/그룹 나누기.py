T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    team = [i for i in range(N+1)]
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    for i in range(M):
        if arr[2*i] > arr[2*i+1]:
            arr[2*i], arr[2*i+1] = arr[2*i+1], arr[2*i]
    for i in range(len(arr)):
        if i % 2:
            arr2.append(arr[i])
        else:
            arr1.append(arr[i])
    for i in range(M):
        for j in range(1, N+1):
            if j == arr2[i]:
                for k in range(1, N+1):
                    if team[j] == team[k]:
                        team[k] = team[arr1[i]]
    team = set(team)
    print(f'#{tc+1} {len(team)-1}')

    
