for tc in range(10):
    N = int(input())
    Numbers = [list(map(int, input().split())) for _ in range(100)]
    x, y = 0, 0
    while y != 99:
        if 0 < x < 100 and Numbers[y][x-1] == 1:
            x = x - 1
        elif 0 <= x < 99 and Numbers[y][x+1] == 1:
            x = x + 1
        else:
            y = y + 1
        Numbers[x][y] = 0
        # Numbers[x][y] == 2 라는 조건문이 필요
    print(f'{N} {x}')
