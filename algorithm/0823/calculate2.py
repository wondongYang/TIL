for tc in range(10):
    N = int(input())
    s1 = input()

    # 후위표기하기
    stack1 = []
    s2 = ''
    for x in s1:
        if '0' <= x <= '9':
            s2 += x
        else:
            stack1.append(x)
    while stack1:
        s2 += stack1.pop()

    # 곱셈 계산하기
    stack1 = []
    stack2 = []
    for x in s2:
        if x == '+':
            stack2.append(stack1.pop())
            stack2.append(x)
        elif x == '*':
            op1 = stack1.pop()
            op2 = stack1.pop()
            stack1.append(op2 * op1)
        else:
            stack1.append(int(x))
    stack2.append(stack1.pop())

    # 덧셈 계산하기
    stack1 = stack2[:]
    for x in stack1:
        if x == '+':
            op1 = stack2.pop(0)
            stack2.pop(0)
            op2 = stack2.pop(0)
            stack2.insert(0, op2 + op1)
    print(f'#{tc+1} {stack2.pop()}')
