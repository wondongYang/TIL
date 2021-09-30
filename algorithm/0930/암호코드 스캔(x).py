change_num16 = [
    '0', '1', '2', '3', 
    '4', '5', '6', '7', 
    '8', '9', 'A', 'B', 
    'C', 'D', 'E', 'F'
]

password = [
    [2,1,1], [2,2,1], [1,2,2], [4,1,1], [1,3,2], 
    [2,3,1], [1,1,4], [3,1,2], [2,1,3], [1,1,2]
]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    code_list16 = [[]]

    # 16진수의 암호코드를 모두 받아오기
    for i in range(N):
        code16 = []
        for j in range(M):
            if arr[i][j] != '0':
                code16.append(arr[i][j])
            if len(code16) != 0 and arr[i][j] == '0' and arr[i][j-1] == '0':
                K = 0
                for j in range(len(code_list16)):
                    if code_list16[j] == code16:
                        K += 1
                        code16 = []
                if K == 0:
                    code_list16.append(code16)
                    code16 = []
        K = 0
        for j in range(len(code_list16)):
            if code_list16[j] == code16:
                K += 1
        if K == 0:
            code_list16.append(code16)
    code_list16.pop(0)

    # 16진수의 암호코드를 10진수로 변경
    code_list10 = []
    for i in range(len(code_list16)):
        code10 = []
        for j in code_list16[i]:
            for k in range(len(change_num16)):
                if j == change_num16[k]:
                    code10.append(k)
        code_list10.append(code10)

    # 10진수의 암호코드를 2진수로 변경
    code_list2 = []
    for i in range(len(code_list10)):
        sum_code2 = ''
        for j in code_list10[i]:
            code2 = ''
            if j == 0:
                code2 += '0000'
            else: 
                while j > 0:
                    if j >= 2**3:
                        code2 += '1'
                        j -= 2**3
                    else:
                        code2 += '0'
                    if j >= 2**2:
                        code2 += '1'
                        j -= 2**2
                    else:
                        code2 += '0'
                    if j >= 2**1:
                        code2 += '1'
                        j -= 2**1
                    else:
                        code2 += '0' 
                    if j >= 2**0:
                        code2 += '1'
                        j -= 2**0
                    else:
                        code2 += '0'
            sum_code2 += code2
        code_list2.append(sum_code2)

    # 2진수의 코드를 정수형으로 변환하여 리스트에 각각 넣기
    big_ans_list = []
    for i in range(len(code_list2)):
        small_ans_list = []
        for j in range(len(code_list2[i])):
            small_ans_list.append(int(code_list2[i][j]))
        big_ans_list.append(small_ans_list)
    
    # 리스트에 들어간 2진수의 코드를 암호코드의 숫자 비율로 만들기
    check_list = []
    for i in range(len(big_ans_list)):
        check_code = []
        count = 0
        for j in range(len(big_ans_list[i])-1, -1, -1):
            if len(check_code) == 0:
                if big_ans_list[i][j] == 1:
                    count += 1
                else:
                    if j != len(big_ans_list[i])-1 and big_ans_list[i][j] != big_ans_list[i][j+1]:
                        check_code.insert(0, count)
                        count = 1
            else: 
                if j != len(big_ans_list[i])-1 and big_ans_list[i][j] != big_ans_list[i][j+1]:
                    check_code.insert(0, count)
                    count = 1
                else:
                    count += 1
        check_code.insert(0, 0)
        check_list.append(check_code)

    # 0과 1의 비율을 4개씩 끊어 리스트 만들기
    ratio_list = []
    for i in range(len(check_list)):
        ratio_check = []
        ratio_code = []
        ratio_num = 0
        for j in range(len(check_list[i])):
            if j // 4 == ratio_num:
                ratio_code.append(check_list[i][j])
            if len(ratio_code) == 4:
                ratio_check.append(ratio_code)
                ratio_num += 1
                ratio_code = []
        ratio_list.append(ratio_check)
        
    # 첫번째 자리가 0임으로 인해 입력 x -> 첫번째 숫자 제거
    for i in range(len(ratio_list)):
        for j in range(len(ratio_list[i])):
            ratio_list[i][j].pop(0)

    print(f'#{tc+1}', end = ' ')
    
    # 비율 리스트를 암호코드 숫자와 대입
    final_check_list = []
    for i in range(len(ratio_list)):
        final_check = []
        for j in range(len(ratio_list[i])):
            for k in range(len(password)):
                for t in range(9):
                    if ratio_list[i][j] == t * password[k]:
                        final_check.append(k)
        final_check_list.append(final_check)

    # 유효성 검증
    check_ans_list = []
    for i in range(len(final_check_list)):
        check_ans = final_check_list[i][-1]
        for j in range(len(final_check_list[i])-1):
            if j % 2 == 0:
                check_ans += 3 * final_check_list[i][j]
            else: 
                check_ans += final_check_list[i][j]
        check_ans_list.append(check_ans)

    # 결과 출력    
    ans_count = 0
    for i in range(len(check_ans_list)):
        if check_ans_list[i] % 10 == 0:
            print(f'{sum(final_check_list[i])}')
            ans_count += 1
            break
    if ans_count == 1:
        continue
    else:
        print('0')
        
'''
password와의 대입에서 문제 발생
0, 0, 0에서 0을 해결하기 위해 첫 자리를 없앤 것에서 문제 발생
'''
            