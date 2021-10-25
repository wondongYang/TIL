T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans_list = [[0] * (2*N) for _ in range(2*N)]    # 4개의 영역 만들기
    for i in range(N):
        for j in range(N):
            ans_list[i][j] = arr[i][j]  # A 영역 채우기
            ans_list[i][-1-j] = arr[i][j]   # B 영역 채우기
            ans_list[-1 - i][j] = arr[i][j]  # C 영역 채우기
            ans_list[-1-j][-1-i] = arr[i][j]    # D 영역 채우기
    print(f'#{tc+1}')
    for i in range(2*N):
        for j in range(2*N):
            print(ans_list[i][j], end = ' ')
        if i != 2*N-1:  # 마지막 행을 출력한 후 띄워쓰기를 하지않기
            print()


'''
2
1
1
2
1 2
3 4

#1
1 1 
1 1 
#2
1 2 2 1 
3 4 4 3 
3 4 4 2 
1 2 3 1 
'''