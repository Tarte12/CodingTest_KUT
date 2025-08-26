def solution(left, right):
    answer = 0
    cnt = 0
    for i in range(left, right+1):
        for num in range(1, i):
            if i % num == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
            cnt = 0
        else:
            answer -= i
            cnt = 0
        
    return answer*(-1)