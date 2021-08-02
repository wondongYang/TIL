# 재귀
def fib(n):
    # base case
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


# 반복문
def fibo_for(n):
    if n < 2:
        return n

    a, b = 0, 1
    
    for i in range(n-1):
        a, b = b, a+b
    return b
print(fibo_for(4))
