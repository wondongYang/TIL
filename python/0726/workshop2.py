# 혈액형 분류하기

def count_blood(a):
    count_A = 0
    count_B = 0
    count_O = 0
    count_AB = 0
    for i in range(0, len(a)):
        if a[i] == 'A':
            count_A += 1
        elif a[i] == 'B':
            count_B += 1
        elif a[i] == 'O':
            count_O += 1
        elif a[i] == 'AB':
            count_AB += 1
    return print({'A': count_A, 'B': count_B, 'O': count_O, 'AB': count_AB})




count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
]) #=> {'A': 3, 'B': 3, 'O': 3, 'AB': 3}