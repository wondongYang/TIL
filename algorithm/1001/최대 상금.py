def max_money(list, c):
    pass

T = int(input())
for tc in range(T):
    num, exchange = input().split()
    num_list = list(int(num))
    num_list2 = num_list[:]
    arr = []
    max_num = 0
    for i in range(len(num_list)):
        for j in num_list2:
            if j > max_num:
                max_num = j
        arr.append(max_num)
        num_list2.remove(max_num)
    print(arr)
        
        
        
    
    
    
 