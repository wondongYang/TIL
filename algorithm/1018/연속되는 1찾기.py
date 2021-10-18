# 16진수를 10진수로 변환하기 위해 리스트의 인덱스 활용
list_16 = [
    '0', '1', '2', '3',
    '4', '5', '6', '7', 
    '8', '9', 'A', 'B', 
    'C', 'D', 'E', 'F'
]

T = int(input())
for tc in range(T):
    N = int(input())
    num16 = list(input())

    # 16진수의 숫자들을 10진수로 변환
    num10 = []
    for i in range(len(num16)):
        for j in range(len(list_16)):
            if num16[i] == list_16[j]:
                num10.append(j)
    
    # 10진수의 숫자들을 2진수로 변환
    num2 = ''
    for i in range(len(num10)):
        a = ''
        k = num10[i]
        while k > 0:
            if k >= 2**3:     # 16진수에서 넘어왔기에 2**4미만의 숫자만 존재
                a += '1'
                k -= 2**3
            else:
                a += '0'
            if k >= 2**2:
                a += '1'
                k -= 2**2
            else:
                a += '0'
            if k >= 2**1:
                a += '1'
                k -= 2**1
            else:
                a += '0'
            if k >= 2**0:
                a += '1'
                k -= 2**0
            else:
                a += '0'
        num2 += a
    
    # 연속하는 1의 개수 세기
    ans_list = [0] * 9
    c = 0
    for i in range(len(num2)):
        if num2[i] == '1':
            c += 1
        else:
            if c != 0:
                for j in range(1, 10):
                    if c == j:
                        ans_list[j-1] += 1
                        c = 0
        if i == len(num2) - 1:
            if c != 0:
                for j in range(1, 10):
                    if c == j:
                        ans_list[j-1] += 1

    # 결과 출력 하기                    
    print(f'#{tc+1}', end = ' ')
    for i in range(len(ans_list)):
        print(f'{ans_list[i]}', end = ' ')
    print()
 
    
