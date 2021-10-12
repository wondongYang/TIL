T = int(input())
for tc in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * (N ** 2)
    for i in range(1, N**2):
        if abs(room.index(i) - room.index(i+1)) == 1:
            visit[i] = 1
    print(visit)
    
        
        
