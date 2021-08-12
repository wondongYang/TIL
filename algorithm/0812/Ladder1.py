for tc in range(10):
    N = int(input())
    Numbers = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = Numbers[y].index(2)
    while y != 0:
        if 0 < x < 100 and Numbers[y][x-1] == 1:
            x = x - 1
        elif 0 <= x < 100 and Numbers[y][x+1] == 1:
            x = x + 1
        else:
            y = y - 1
        Numbers[y][x] = 0
    print(f'#{N} {x}')

