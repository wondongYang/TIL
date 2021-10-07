T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr.pop(0)
    check_list = []
    c = 0
    while len(arr) > 0:
        max_charge = 0
        for i in range(1, len(arr)+1):
            if arr[-i] >= i and i >= max_charge:
                max_charge = i
        if max_charge == len(arr):
            break
        c += 1
        for i in range(max_charge):
            arr.pop()
    print(f'#{tc+1} {c}')
        