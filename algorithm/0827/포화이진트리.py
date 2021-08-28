# 포화이진트리


def pre_order(n, last):
    if n <= last:
        print(n, end = ' ')          # n에서 처리할 일
        pre_order(n*2, last)
        pre_order(n*2+1, last)

last = 8
tree = []