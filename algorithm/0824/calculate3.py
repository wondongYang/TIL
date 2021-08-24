def arr(s1):

    # 후위 연산하기
    stack = []
    s2 = ''
    for x in s1:
        if '0' <= x <= '9':
            s2 += x
        elif x == '(':
            stack.append(x)
        elif x == ')':
            p = stack.pop()
            while p != '(':
                s2 += p
                p = stack.pop()
        elif x == '*':
            while stack and stack[-1] == "*":
                s2 += stack.pop()
            stack.append(x)
        elif x == '+':
            while stack and stack[-1] != '(':
                s2 += stack.pop()
            stack.append(x)
    while stack:
        s2 += stack.pop()

    # 후위 연산한 식을 계산하기
    for x in s2:
        if x == '+':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 + op1)
        elif x == '*':
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2 * op1)
        else:
            stack.append(int(x))
    return stack.pop()

for tc in range(10):
    N = int(input())
    s1 = input()
    ans = arr(s1)
    print(f'#{tc+1} {ans}')

