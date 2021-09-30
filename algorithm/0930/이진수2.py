T = int(input())
for tc in range(T):
    N = float(input())
    count = 0
    K = ''
    while N > 0:
        if count == 12:
            count += 1
            break
        if N >= 2**(-1-count):
            K += '1'
            N -= 2**(-1-count)
        else:
            K += '0'
        count += 1
    if count > 12:
        print(f'#{tc+1} overflow')     
    else:
        print(f'#{tc+1} {K}')

'''
3
0.625
0.1
0.125
'''