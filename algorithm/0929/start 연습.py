T = int(input())
for tc in range(T):
    arr1 = list(map(int, input()))
    # 7개씩 잘라 b6~b0으로 사용...
    arr2 = [[0] * 7 for _ in range(10)]
    t = 0
    for i in range(10):
        for j in range(7):
            arr2[i][j] = arr1[t]
            t += 1
    print(f'#{tc+1}', end = ' ')
    for i in range(10):
        ans = 0
        for j in range(7):
            if arr2[i][j] == 1:
                ans += 2**(6-j)
        print(f'{ans}', end= ' ')
    print()

'''
1
0000000111100000011000000111100110000110000111100111100111111001100111
0000010101110001010100111001110000110101101001010001000000010100110011
1001110111000001100111111111011110110111000010100110100111000000000010
'''