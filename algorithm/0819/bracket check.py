T = int(input())
for tc in range(T):
    s = input()
    stack = []
    top = -1
    ans = 1
    for x in s:
        if x == '(' or x == '{':
            top += 1
            stack.append(x)
        elif x == ')':
            if stack and stack[top] == '(':
                top -= 1
                stack.pop()
            else:
                ans = 0
                break
        elif x == '}':
            if stack and stack[top] == '{':
                top -= 1
                stack.pop()
            else:
                ans = 0
                break
    if ans and stack:
        ans = 0
    print(f'#{tc+1} {ans}')


