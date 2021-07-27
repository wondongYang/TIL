# 숫자의 의미

def lonely(a):
    list_a = []
    for i in range(0, len(a)-1):
        if a[i] != a[i+1]:
            list_a.append(a[i])
    list_a.append(a[len(a)-1])
    return print(list_a)    




lonely([1, 1, 3, 3, 0, 1, 1]) #=> [1, 3, 0, 1]
lonely([4, 4, 3, 3, 3]) #=> [4, 3]