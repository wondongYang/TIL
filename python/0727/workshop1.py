# 무엇이 중복일까

def duplicated_letters(a):
    list_a = list(a)
    same_count = {}
    list_duplicated = []
    for i in list_a:
        if i in same_count:
            same_count[i] += 1
        else:
            same_count[i] = 1
    for key, value in same_count.items():
        if value > 1:
            list_duplicated.append(key)
    return print(list_duplicated)

duplicated_letters('apple') #=> ['p']
duplicated_letters('banana') #=> ['a', 'n']