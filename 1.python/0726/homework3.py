# 정사각형만 만들기

def only_square_area(a, b):
    square_list = []
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                square_list.append(a[i]*b[j])
    return print(square_list)

only_square_area([32, 55, 63], [13, 32, 40, 55]) #=> [1024, 3025]