for tc in range(10):
    D_count = int(input())
    box_list = list(map(int, input().split()))
    for j in range(D_count):
        max_box = 0
        min_box = 100
        for i in range(len(box_list)):
            if box_list[i] > max_box:
                max_box = box_list[i]
            if box_list[i] < min_box:
                min_box = box_list[i]
        box_list[box_list.index(max_box)] = max_box - 1
        max_box -= 1
        box_list[box_list.index(min_box)] = min_box + 1
        min_box += 1
    last_max_box = 0
    last_min_box = 100
    for k in range(len(box_list)):
        if box_list[k] > last_max_box:
            last_max_box = box_list[k]
        if box_list[k] < last_min_box:
            last_min_box = box_list[k]
    diff_box = last_max_box - last_min_box
    print(f'#{tc+1} {diff_box}')