'''
1
10 6 12 8 9 4 1 3
'''

for tc in range(10):
    T = int(input())
    code = list(map(int, input().split()))
    num = [1, 2, 3, 4, 5]
    k = 0
    while code[-1] > 0:
        f1 = code.pop(0)
        f8 = f1 - num[k%5]
        if f8 < 0:
            f8 = 0
        code.append(f8)
        k += 1
    print(f'#{T}', end=' ')
    for i in code:
        print(i, end=' ')
    print()






