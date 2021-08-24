T = int(input())
for tc in range(T):
    s1 = list(input().split())
    stack = []
    print(f'#{tc+1}', end=' ')
    for x in s1:
        if '0' <= x <= '9':
            stack.append(int(x))
        elif len(stack) > 1:
            if x == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 + op1)
            elif x == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif x == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 * op1)
            elif x == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 / op1)
            elif x == '.':
                print('error')
        elif x == '.':
            print(int(stack[0]))
        else:
            print('error')
            break