T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, str(input())))
    dict_arr = {}
    max_count_number = 0
    max_count = 0
    for i in range(len(arr)):
        dict_arr[arr[i]] = arr.count(arr[i])
        if dict_arr[arr[i]] >= max_count:
            if arr[i] > max_count_number:
                max_count_number = arr[i]
                max_count = dict_arr[arr[i]]
    print(f'#{tc+1} {max_count_number} {max_count}')



