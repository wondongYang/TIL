T = int(input())
for tc in range(T):
    A, B = input().split()
    count = 0
    for i in range(len(A)-len(B)+1):
        if A[i] == B[0]:
            check = 1
            for j in range(1, len(B)):
                if A[i + j] == B[j]:
                    check += 1
            if check == len(B):
                count += 1
    typing = len(A) - (count * (len(B) - 1))
    print(f'#{tc+1} {typing}')

