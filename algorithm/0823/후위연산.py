s1 = '2+3*4/5'

# step1
stack = []
s2 = ''
for x in s1:
    if '0' <= x <= '9':
        s2 += x
    else:
        stack.append(x)
while stack:
    s2 += stack.pop()
print(s2)


# step2
stack = []
for x in s2:
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
    else:
        stack.append(int(x))
print(stack.pop())