def my_func(a):
    try:
        result = int(a)
        return result
    except:
        return False
    finally:
        print(a)

print(my_func('3.5'))

def my_func2(a):
    try:
        result = int(a)
        return result
    except:
        return False
    print(a)

print(my_func2('3.5'))