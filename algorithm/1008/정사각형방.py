T = int(input())
for tc in range(T):
    N = int(input())
    room = [list(map(int, input().split()))]
    visit = [0] * (N ** 2)
    con_num = 1
    max_num = 0
    small_num = N**2
    for i in range(1, N**2):
        if abs(room.index(i) - room.index(i+1)) == 1:
            con_num += 1
            small_num = i
        else:
            con_num = 1
        
        
        

