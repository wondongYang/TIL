# 복사가 잘 된건가?

a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(a) #=> [1, 2, 5, 4, 5]
print(b) #=> [1, 2, 5, 4, 5]