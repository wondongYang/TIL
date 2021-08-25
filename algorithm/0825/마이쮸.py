p = 1  # 처음 줄 설 사람 번호
q = []
N = 20  # 초기 마이쮸 개수
my = [0] * (N+1)
cnt = [0] * (N+1)
m = 0   # 나눠준 개수
v = 0
while m<N:

    q.append(p)
    cnt[p] += 1
    input()  # 엔터를 치면
    print(f'큐에 있는 사람 수 : {len(q)}, {q}')

    #input()
    v = q.pop(0) # 받을 사람 v
    m += cnt[v]  # 줄선 횟수 만큼 배분
    print(f'받을 사람 : {v} , 받을 개수 : {cnt[v]}')
    my[v] += cnt[v]  # 받은 개수

    print(f'나눠준 개수 : {min(m, N)}')  # 실제 가능한 배분 개수 선택

    q.append(v) # 받은 사람이 다시 줄서면
    cnt[v] += 1
    p += 1      # 따라 들어갈 사람 번호
    for i in range(1, p):
        print(f'{i} : {my[i]}, ', end=' ')
    print()
print(f'마지막 받은 사람 : {v}')