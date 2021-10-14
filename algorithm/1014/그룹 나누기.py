T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    for i in range(len(arr)):
        if i % 2:
            arr2.append(arr[i])
        else:
            arr1.append(arr[i])
    
