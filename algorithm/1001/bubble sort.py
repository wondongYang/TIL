def bubble_sort(a, n, c):
    # 자리를 바꾸기 위해 새로운 a를 지정
    new_a = a[:]
    for _ in range(n):
        for j in range(n-1):

            # 내림차순으로 정렬하기 위해 자리를 변경
            if a[j] < a[j+1]:
                a[j+1] = new_a[j]
                a[j] = new_a[j+1]

                # a가 변경될 때 마다 새로운 a를 다시 지정
                new_a = a[:]
                c += 1
    return new_a

a = [3, 2, 8, 8, 8]
n = len(a)
max_c = 0
print(bubble_sort(a, n, max_c))
print(max_c)