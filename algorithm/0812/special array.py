T = int(input())
for tc in range(T):
    N = int(input())
    Numbers = list(map(int, input().split()))
    ans_list = []
    for i in range(N):
        if i % 2 == 0:
            ans_list.append(max(Numbers))
            Numbers.remove(max(Numbers))
        else:
            ans_list.append(min(Numbers))
            Numbers.remove(min(Numbers))
    print(f'#{tc+1}' , end = ' ')
    print(*ans_list[:10])