T = int(input())
for tc in range(T):
    num2 = list(map(int, input()))
    num3 = list(map(int, input()))
    change_num2 = []
    change_num3 = []

    # 2진수를 한자리수 바꾸기
    for i in range(len(num2)):
        l = num2[:]
        if num2[i] == 0:
            l[i] = 1
            change_num2.append(l)
        else:
            l[i] = 0
            change_num2.append(l)
    
    # 3진수를 한자리수 바꾸기
    for i in range(len(num3)):
        l = num3[:]
        if num3[i] == 0:
            l[i] = 1
            change_num3.append(l)
            l = num3[:]
            l[i] = 2
            change_num3.append(l)
        elif num3[i] == 1:
            l[i] = 0
            change_num3.append(l)
            l = num3[:]
            l[i] = 2
            change_num3.append(l)
        else:
            l[i] = 0
            change_num3.append(l)
            l = num3[:]
            l[i] = 1
            change_num3.append(l)

    # 2진수와 3진수를 10진수로 표현
    nature2 = []
    nature3 = []
    for i in range(len(change_num2)):
        K = 0
        for j in range(len(change_num2[i])):
            if change_num2[i][j] != 0:
                K += 2 ** (len(change_num2[i])-1-j)
        nature2.append(K)
    for i in range(len(change_num3)):
        K = 0
        for j in range(len(change_num3[i])):
            if change_num3[i][j] != 0:
                K += change_num3[i][j] * (3 ** (len(change_num3[i])-1-j))
        nature3.append(K)
    
    # nature2에 있는 숫자 중 nature3에 있는 숫자 찾기
    def binary_search(l, r, num):
        if l > r:
            return
        m = (l+r)//2
        if nature2[m] == num:     # 같으면
            return num
        elif nature2[m] < num:    # 오른쪽 구간 선택
            return binary_search(m+1, r, num)
        else:               # 왼쪽 구간 선택
            return binary_search(l, m-1, num)

    nature2.sort()
    ans_list = []
    for i in nature3:
        ans = binary_search(0, len(nature2)-1, i)
        if ans:
            ans_list.append(ans)

    print(f'#{tc+1} {ans_list[0]}')


    