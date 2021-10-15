N, M = map(int, input().split())
if M == 1:
    for i in range(1, 7):
        ans = []
        ans.append(i)
        for j in range(1, 7):
            ans.append(j)
            for k in range(1, 7):
                ans.append(k)
                print(*ans)
                ans.pop()
            ans.pop()
        ans.pop()
    
elif M == 2:
    for i in range(1, 7):
        ans = []
        ans.append(i)
        for j in range(1, 7):
            if i <= j:
                ans.append(j)
            for k in range(1, 7):
                if i <= j <= k:
                    ans.append(k)
                    print(*ans)
                    ans.pop()
            if i <= j:
                ans.pop()  
        ans.pop() 
else:
    for i in range(1, 7):
        ans = []
        ans.append(i)
        for j in range(1, 7):
            if i != j:
                ans.append(j)
            for k in range(1, 7):
                if i != j and i != k and j != k:
                    ans.append(k)
                    print(*ans)
                    ans.pop()
            if i != j:
                ans.pop()  
        ans.pop() 