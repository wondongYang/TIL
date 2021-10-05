T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0       # 화물차 이용 횟수
    while len(arr) > 0:     # 이용할 수 있는 경우가 남아있다면 
        min_finish = 24
        for i in range(len(arr)):   # 가장 먼저 끝나는 시간을 찾아
            if arr[i][1] <= min_finish:
                min_finish = arr[i][1]
        for i in range(len(arr)):   # min 보다 먼저 시작하는 작업을 처리
            if arr[i][0] < min_finish:
                arr[i][1] = 0
        k = len(arr)
        for i in range(k):  # min 보다 먼저 시작하는 작업을 삭제
            i = i + len(arr) - k    # pop 연산을 하기 위해 사용
            if arr[i][1] == 0:
                arr.pop(i)
        count += 1
    print(f'#{tc+1} {count}')


'''
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
'''