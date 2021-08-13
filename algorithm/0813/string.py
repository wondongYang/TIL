# atoi, itoa

def my_atoi(s):
    i = 0
    if s[0] == '-':
        1
    elif s[0] == '+':
        1
    else:
        for x in s:
            i = i*10 + ord(x)-ord('0')
    return i

def my_itoa(i):
    s = ''
    while i > 0:
        s += chr(i%10 + ord('0'))
        i //= 10
    s = s[::-1]
    return s

a = '123'
b = my_atoi(a)
print(b)

c = 456
print(my_itoa(c))