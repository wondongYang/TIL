def f(A):
    for i in range(1, 1 << 10): # 10개원소의 포함여부 표시
        s = 0
        for j in range(10):
            if i & (1 << j): # i의 j번 비트가 1이면 A[j]원소가 부분집합에 포함
                s += A[j]
                if s == 0:
                    return 1
    return 0

T = int(input())
for tc in range(T):
    Numbers = list(map(int, input().split()))
    print(f'#{tc+1} {f(Numbers)}')