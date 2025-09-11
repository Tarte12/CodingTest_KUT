n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

lt = max(money) #최소 max(money) 이상이어야 함
rt = sum(money) #1번 뽑아서 해결하겠다
count = 0 #m번만 인출할 거 체크
answer = 0 #정답

while lt <= rt: #K(mid)값 구하는 while문
    
    if m == 1:
        print(rt)
        exit()
    if m >= n:
        print(lt)
        exit()

    mid = (lt+rt)//2 #정답 후보
    wallet = mid
    count = 1
    
    for cost in money: #하루 동안 쓸 cost 체크
        if cost > wallet:
            wallet = mid - cost
            count += 1
        else:
            wallet -= cost
    
    if count > m: #해당 mid값으로는 m번 인출 조건 만족 X
        lt = mid + 1 
    else:
        answer = mid
        rt = mid - 1
print(answer)