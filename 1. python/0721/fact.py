def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
        print(result)
    return result
    
# print(fact(3)) # 6
# print(fact(4))

# 재귀
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(4))