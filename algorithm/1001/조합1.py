c = 0
for i in range(8):
    for j in range(i+1, 9):
        for k in range(j+1, 10):
            c += 1
            print(c, i, j, k)