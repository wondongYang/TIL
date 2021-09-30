change_num16 = [
    '0', '1', '2', '3', 
    '4', '5', '6', '7', 
    '8', '9', 'A', 'B', 
    'C', 'D', 'E', 'F'
]

T = int(input())
for tc in range(T):
    N, num_16 = input().split()
    list_16 = list(num_16)
    list_10 = []
    for i in range(len(list_16)):
        for j in range(len(change_num16)):
            if list_16[i] == change_num16[j]:
                list_10.append(j)
    ans = ''
    for i in range(int(N)):
        K = ''
        if list_10[i] == 0:
            K = '0000'
        else:
            while list_10[i] > 0:
                if list_10[i] >= 2**3:
                    K += '1'
                    list_10[i] -= 2**3
                else:
                    K += '0'
                if list_10[i] >= 2**2:
                    K += '1'
                    list_10[i] -= 2**2
                else:
                    K += '0'
                if list_10[i] >= 2**1:
                    K += '1'
                    list_10[i] -= 2**1
                else:
                    K += '0' 
                if list_10[i] >= 2**0:
                    K += '1'
                    list_10[i] -= 2**0
                else:
                    K += '0'
        ans += K
    print(f'#{tc+1} {ans}')

'''
3
4 47FE
5 79E12
8 41DA16CD
'''