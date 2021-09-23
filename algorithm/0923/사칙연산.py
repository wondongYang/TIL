def f(n):
    if len(tree[n]) == 1:
        return tree[n][0]
    else:
        if tree[n][0] == '+':
            return f(tree[n][1]) + f(tree[n][2])
        elif tree[n][0] == '-':
            return f(tree[n][1]) - f(tree[n][2])
        elif tree[n][0] == '*':
            return f(tree[n][1]) * f(tree[n][2])
        elif tree[n][0] == '/':
            return f(tree[n][1]) // f(tree[n][2])
 
for tc in range(10):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        data = input().split()
        if len(data) == 2:                                           
            tree[int(data[0])] = [int(data[1])]                      
        else:                                                        
            tree[int(data[0])] = [data[1]]+list(map(int, data[2:]))
     
    print(f'#{tc+1} {f(1)}')