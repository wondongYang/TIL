T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    group = [i for i in range(N+1)]
    arr = [list(map(int, input().split())) for _ in range(M)]
    arr1 = []
    arr2 = []
    for i in range(M):
        if len(arr[i]) == 1:
            arr[i].append(arr[i][0])
    for i in range(M):
        if arr[i][0] > arr[i][1]:
            arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
    for i in range(len(arr)):
        arr1.append(arr[i][0])
        arr2.append(arr[i][1])
    for i in range(M):
        for j in range(1, N+1):
            if j == arr2[i]:
                for k in range(1, N+1):
                    if group[j] == group[k]:
                        group[k] = group[arr1[i]]
    group = set(group)
    print(f'#{tc+1} {len(group)-1}')