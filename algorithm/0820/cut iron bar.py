T = int(input())
for tc in range(T):
    s = input()
    stack = []
    top = -1
    piece = 0
    for i in range(len(s)):
        if s[i] == '(':
            top +=1
            stack.append(s[i])
        elif s[i] == ')':
            top -= 1
            stack.pop()
            if s[i-1] == '(':
                piece += len(stack)
            elif s[i-1] == ')':
                piece += 1
    print(f'#{tc+1} {piece}')

