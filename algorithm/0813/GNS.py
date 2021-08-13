T = int(input())
for tc in range(T):
    TC, N = input().split()
    Numbers = list(input().split())
    str_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in range(len(str_list)):
        count = 0
        for j in range(int(N)):
            if Numbers[j] == str_list[i]:
                count += 1
        str_list[i] = (str_list[i], count)
    print(TC)
    final = ''
    for i in range(len(str_list)):
        final += str_list[i][0] * str_list[i][1]
    for i in range(len(final)):
        print(final[i], end = '')
        if i % 3 == 2:
            print(' ', end = '')

