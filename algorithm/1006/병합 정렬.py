def mergesort(arr):
    if len(arr) <= 1:
        return arr
    L_arr = mergesort(arr[:len(arr)//2])
    R_arr = mergesort(arr[len(arr)//2:])
    return merge(L_arr, R_arr)

def merge(L_arr, R_arr):
    global c
    if L_arr[-1] > R_arr[-1]:
        c += 1
    
    Sum_arr = []
    L_index, R_index = 0, 0
    while L_index < len(L_arr) or R_index < len(R_arr):
        if L_index < len(L_arr) and R_index < len(R_arr):
            if L_arr[L_index] < R_arr[R_index]:
                Sum_arr.append(L_arr[L_index])
                L_index += 1
            else:
                Sum_arr.append(R_arr[R_index])
                R_index += 1
        elif L_index < len(L_arr):
            Sum_arr.append(L_arr[L_index])
            L_index += 1
        elif R_index < len(R_arr):
            Sum_arr.append(R_arr[R_index])
            R_index += 1
 
    return Sum_arr


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    c = 0
    print(f'#{tc+1} {mergesort(arr)[N//2]} {c}')
        